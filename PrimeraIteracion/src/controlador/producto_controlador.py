from wtforms import form
from modelo._db import db
from flask import render_template, redirect, url_for, request, flash, session
from modelo.producto import Producto
from modelo.crear import Crear

from templates.CrearProducto.forms import ProductForm

def crear():
  product_form = ProductForm(request.form)
  if request.method == 'GET':
    return render_template('CrearProducto/crear_producto.html', form = product_form)
  
  if request.method == 'POST' and product_form.validate():
    nombre = product_form.nombre.data
    descripcion = product_form.descripcion.data
    imagen = product_form.imagen.data
    precio = product_form.precio.data
    palabras_clave = product_form.palabras_clave.data

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

  print(productos)

  return render_template('MisProductos/misPublicaciones.html', title='Mis Publicaciones', 
                          productos=productos, name=session['usuario'])
