import sys
import os
from flask import render_template, redirect, url_for, request, abort, jsonify, flash, session
from modelo.producto import Producto, db, ma
from modelo.crear import Crear
import json

class ProductoEsquema(ma.Schema):
  class Meta:
    fields = ['id', 'nombre', 'descripcion','imagen', 
              'precio', 'palabras_clave', 'cantidad_vendidos']

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

def crear():
  """Crea un producto."""
  return render_template('crear_producto.html')

def create_product():
  nombre = request.form['nombre']
  descripcion = request.form['descripcion']
  imagen = request.form['imagen']
  precio = request.form['precio']
  palabras_clave = request.form['palabras_clave']

  producto_nuevo = Producto(nombre, descripcion, imagen,
                              precio, palabras_clave)

  db.session.add(producto_nuevo)
  db.session.commit()
  db.session.add(Crear(session['usuario'], producto_nuevo.id))
  db.session.commit()

  flash('Se ha creado el producto con éxito')
  return redirect('/producto')

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
    flash('Se ha eliminado el producto con éxito')

    return redirect('/producto')

  if 'actualizar' in request.form:
    id = request.form.get('actualizar')
    producto = Producto.query.get(id)
  
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    imagen = request.form.get('imagen')
    precio = request.form.get('precio')
    palabras_clave = request.form.get('palabras_clave')

    if nombre != '':
      producto.nombre = nombre
    if descripcion != '':
      producto.descripcion = descripcion
    if imagen != '':
      producto.imagen = imagen
    if precio != '':
      producto.precio = precio
    if palabras_clave != '':
      producto.palabras_clave = palabras_clave

    db.session.merge(producto)
    db.session.commit()
    flash('Se ha actualizado el producto con éxito')

    return redirect('/producto')

  productos_id = list(map(lambda x: x.id_producto,
                      Crear.query.filter_by(usuario=session['usuario']).all()))
  productos = [Producto.query.filter_by(id=id).first() for id in productos_id]

  return render_template('misPublicaciones.html', title='Mis Publicaciones', 
                          productos=productos, name=session['usuario'])
