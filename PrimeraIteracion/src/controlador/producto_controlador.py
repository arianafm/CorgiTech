import sys
from flask import Flask, render_template, redirect, url_for, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from modelo.producto import Producto

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)

class ProductoEsquema(ma.Schema):
  class Meta:
    fields = ['id', 'nombre', 'descripcion','imagen', 
              'precio', 'palabras_clave', 'cantidad_vendidos']

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

def actualizar():
  """ Actualiza un producto
      
  """
  id = request.json['id']
  nombre = request.json['nombre']
  descripcion = request.json['descripcion']
  imagen = request.json['imagen']
  precio = request.json['precio']
  palabras_clave = request.json['palabras_clave']

  print(request.json)

  producto = Producto.query.get(id)

  if nombre != None:
    producto.nombre = nombre
  if descripcion != None:
    producto.descripcion = descripcion
  if imagen != None:
    producto.imagen = imagen
  if precio != None:
    producto.precio = 100
  if palabras_clave != None:
    producto.palabras_clave = palabras_clave

  db.session.merge(producto)
  db.session.commit()

  return "Se actualizó con éxito"

def agregar():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    imagen = request.json['imagen']
    precio = request.json['precio']
    palabras_clave = request.json['palabras_clave']
    #cantidad_vendidos = request.json['cantidad_vendidos']
    #id = request.json['id']

    producto_nuevo = Producto(nombre, descripcion, imagen, 
                              precio, palabras_clave)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)

def comprar():
  """ Elimina un producto
      
  """
  return 0

def consultar():
  """ Elimina un producto
      
  """
  return 0

def eliminar():
  """ Elimina un producto
      
  """
  return 0

def index():
  """ Elimina un producto
      
  """
  return jsonify ({'msg': 'Esta es la página de publicaciones'})