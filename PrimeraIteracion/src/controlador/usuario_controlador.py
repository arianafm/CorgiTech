import re
import sys
import random
import string
import modelo.usuario
from flask import Flask, render_template, redirect, url_for, request, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from cryptography.fernet import Fernet
from flask_mail import Mail, Message

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)
fernet = Fernet(b'tJg6ll_KljmoKvledZzcDBFskn7w3OmMokimkGBnFP0=')
mail= Mail(app)
nombre_de_usuario = ''
correo = ''

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

  usuario = request.json['usuario']
  correo = request.json['correo']
  telefono = request.json['telefono']

  usuario_nuevo = modelo.usuario.Usuario(usuario, correo, telefono)

  db.session.add(usuario_nuevo)
  db.session.commit()
  
  return redirect(url_for('usuario_bp.correo_confirmacion'))

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
  mail.send(msg)
  return "Correo enviado."


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

  usuario_login = modelo.usuario.Usuario.query.filter_by(usuario = usuario).first()  

  nombre_de_usuario = usuario_login.usuario
  if(nombre_de_usuario is not None and contrasena == str(fernet.decrypt(usuario_login.contrasena.encode()).decode())):
    return "Bienvenido"
  else:
    return "Sucedio algo"
  
# Creo que este lo vamos a borrar no lo veo muy necesario.
# def coinciden_contrasenas(self, contraseña):
#   return self.contraseña == contraseña

def logout():
  return 0

def index():
  """ Elimina un producto
      
  """
  return jsonify ({'msg': 'Esta es la página de publicaciones'})

