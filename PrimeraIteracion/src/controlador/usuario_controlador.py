import sys
import random
import string
from flask import Flask, render_template, redirect, url_for, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from modelo.usuario import Usuario
import modelo.usuario

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)

class UsuarioEsquema(ma.Schema):
  class Meta:
    fields = ['usuario', 'correo', 'telefono','contrasena']

usuario_esquema = UsuarioEsquema()
usuarios_esquema = UsuarioEsquema(many=True)

def generar_contrasena():
  return 0

#agregar_usuario
def registrar():
  return 0

def login():
  return 0

def coinciden_contrasenas(self, contraseña):
  return self.contraseña == contraseña

def logout():
  return 0

def index():
  """ Elimina un producto
      
  """
  return jsonify ({'msg': 'Esta es la página de publicaciones'})