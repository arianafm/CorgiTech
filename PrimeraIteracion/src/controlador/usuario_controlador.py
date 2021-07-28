import re
import os
import sys
import random
import string
import modelo.usuario
from templates.RegistrarUsuario.forms import CommentForm

from flask.helpers import make_response
from flask import Flask, render_template, redirect, url_for, request, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from cryptography.fernet import Fernet
from flask_mail import Mail, Message

template_dir = os.path.abspath('../../templates')

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)

# Inicializar la clase Fernet con la llave que generamos.
fernet = Fernet(b'tJg6ll_KljmoKvledZzcDBFskn7w3OmMokimkGBnFP0=')
# Creamos una instancia de la clase correo.
mail= Mail(app)

nombre_de_usuario = ''
correo = ''

# Configuraciones pertenecientes a flask_mail.
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'corgitech2021@gmail.com'
app.config['MAIL_PASSWORD'] = 'fbgfqabyxaijedkf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail= Mail(app)

class UsuarioEsquema(ma.Schema):
  class Meta:
    fields = ['usuario', 'correo', 'telefono','contrasena']

usuario_esquema = UsuarioEsquema()
usuarios_esquema = UsuarioEsquema(many=True)

def generar_contrasena():
  """ 
  Función que se encarga de generar una cadena
  aleatoria de longitud 10 y después la cifra.
  """
  contrasena = ''.join(random.sample(string.ascii_lowercase, 10))
  encContrasena = fernet.encrypt(contrasena.encode())
  return encContrasena


def registrar():
  """ 
  Función que dados los datos recabados en el
  JSON que recibimos como petición, se encarga
  de crear un objeto Usuario para después aña-
  dirlo a la base de datos. Al terminar nos 
  redirige a "correo_confirmación".
  """
  global correo

  comment_form = CommentForm(request.form)

  correo = comment_form.correo.data

  if request.method == 'POST' and comment_form.validate():

    try:
      usuario_nuevo = modelo.usuario.Usuario( usuario = comment_form.usuario.data,
                                              correo = comment_form.correo.data,
                                              telefono = comment_form.telefono.data
                                            )
      db.session.add(usuario_nuevo)
      db.session.commit()
    except:
      db.session.rollback()
      raise abort(500, 'Ocurrió un error al añadir el registro del usuario a la base de datos.')
    
    return redirect(url_for('usuario_bp.correo_confirmacion'))
    
  else:
    return render_template('/RegistrarUsuario/index.html', form = comment_form)


def correo_confirmacion():
  """ 
  Función que manda un correo de confirmación
  de registro al usuario que se acaba de regis-
  trar. El correo incluye nombre de usuario y
  contraseña ya descifrada, recordemos que esta
  última es generada por el propio sistema con
  la ayuda de "generar_contrasena()".
  """
  usuario_actual = modelo.usuario.Usuario.query.filter_by(correo = correo).first()
  msg = Message('MercaTodo: Correo de confirmación', sender = 'corgitech2021@gmail.com', recipients = [usuario_actual.correo])
  msg.body =  'Gracias por crear su cuenta en MercaTodo.\n' + 'Su contrasena para acceder al sistema es:\n' + str(fernet.decrypt(usuario_actual.contrasena.encode()).decode())

  try:
    mail.send(msg)
  except:
    db.session.query(modelo.usuario.Usuario).filter_by(correo=correo).delete()
    db.session.commit()
    raise abort(500, 'Ocurrió un error al intentar enviar correo de confirmación al usuario. Intente hacer nuevamente su registro.')

  return render_template('/ConfirmacionRegistro/index.html', correo=correo)


def login():
  """ 
  Función que dados los datos recabados en el
  JSON que recibimos como petición (usuario y
  contrasena) hace la busqueda del usuario en
  la base de datos para posteriormente si se
  encuentra al usuario y su contraseña es co-
  rrecta le de acceso al sistema, en otro caso
  se le niega el acceso.
  """
  global nombre_de_usuario 

  usuario = request.json['usuario']
  contrasena = request.json['contrasena']

  if(usuario == '' or contrasena == ''):
    abort(400, 'Todos los campos son obligatorios')

  # Nos devuelve un usuario (objeto) dado el usuario de la petición. 
  usuario_login = modelo.usuario.Usuario.query.filter_by(usuario = usuario).first()  

  if(usuario_login is None):
    abort(404, 'El nombre de usuario no está asociado a ningún registro.')

  nombre_de_usuario = usuario_login.usuario

  if(contrasena == str(fernet.decrypt(usuario_login.contrasena.encode()).decode())):
    return "Bienvenido"
  else:
    abort(400, 'La contraseña es incorrecta.')
  

def logout():
  return 0

def index():
  """ Elimina un producto
      
  """
  return jsonify ({'msg': 'Esta es la página de publicaciones'})

