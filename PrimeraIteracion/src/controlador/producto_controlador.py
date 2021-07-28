import sys
import os
from flask import render_template, redirect, url_for, request, abort, jsonify
from modelo.producto import Producto, db, ma

class ProductoEsquema(ma.Schema):
  class Meta:
    fields = ['id', 'nombre', 'descripcion','imagen', 
              'precio', 'palabras_clave', 'cantidad_vendidos']

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

def actualizar():
  """Actualiza un producto."""
  id = request.json['id']
  nombre = request.json['nombre']
  descripcion = request.json['descripcion']
  imagen = request.json['imagen']
  precio = request.json['precio']
  palabras_clave = request.json['palabras_clave']

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

def crear():
    """Crea un producto."""
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    imagen = request.json['imagen']
    precio = request.json['precio']
    palabras_clave = request.json['palabras_clave']

    producto_nuevo = Producto(nombre, descripcion, imagen, 
                              precio, palabras_clave)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)

def comprar():
  """Compra un producto."""
  return 0

def consultar():
  """Consulta un producto."""
  return 0

def index():
  """Página principal de Mis Publicaciones."""

  if 'eliminar' in request.form:
    id = request.form.get('eliminar')
    producto = Producto.query.get(id)
  
    db.session.delete(producto)
    db.session.commit()

    return redirect('/producto')

  return render_template('misPublicaciones.html', title='Mis Publicaciones', productos=Producto.query.all())