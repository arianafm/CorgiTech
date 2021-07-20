import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from modelo.producto import Producto, db, ma

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
  producto = Producto.query.get(request.json['id'])
  
  db.session.delete(producto)
  db.session.commit()

  return "Producto eliminado"

def index():
  """ Elimina un producto
      
  """
  return jsonify ({'msg': 'Esta es la página de publicaciones'})