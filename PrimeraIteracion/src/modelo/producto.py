from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
db = SQLAlchemy()

class Producto(db.Model):
  __tablename__ = 'producto'

  nombre = db.Column(db.Unicode)
  descripcion = db.Column(db.Unicode)
  imagen = db.Column(db.Unicode)
  precio = db.Column(db.Integer)
  palabras_clave = db.Column(db.Unicode)
  cantidad_vendidos = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, nombre, descripcion, imagen, 
               precio, palabras_clave):
    """Crea un nuevo producto

    Comentar parametros
    """
    self.nombre = nombre
    self.descripcion = descripcion
    self.imagen = imagen
    self.precio = precio
    self.palabras_clave = palabras_clave
    self.cantidad_vendidos = 0