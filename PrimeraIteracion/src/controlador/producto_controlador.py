import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from modelo.producto import Producto, db, ma
import json

class ProductoEsquema(ma.Schema):
  class Meta:
    fields = ['id', 'nombre', 'descripcion','imagen', 
              'precio', 'palabras_clave', 'cantidad_vendidos']

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

def actualizar():
  """ Actualiza un producto
      
  """
  return 0

def agregar():
    return render_template('crear_producto.html')

def create_product():
  nombre = request.form['nombre']
  descripcion = request.form['descripcion']
  imagen = request.form['imagen']
  precio = request.form['precio']
  palabras_clave = request.form['palabras_clave']
  #cantidad_vendidos = request.json['cantidad_vendidos']
  #id = request.json['id']

  producto_nuevo = Producto(nombre, descripcion, imagen, 
                              precio, palabras_clave)

  db.session.add(producto_nuevo)
  db.session.commit()

  return render_template('crear_producto.html')

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