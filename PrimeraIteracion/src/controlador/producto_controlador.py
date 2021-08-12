from wtforms import form
from flask import render_template, redirect, url_for, request, flash, session, Flask, abort
from modelo.producto import Producto, search
from modelo.crear import Crear
from modelo.usuario import Usuario
from flask_mail import Mail, Message
import qrcode
from templates.CrearProducto.forms import ProductForm
from templates.Checkout.forms import CForm
from PIL import Image

from modelo._db import db
from _app import app

mail = Mail(app)

def crear():
  """
  Crear un producto a partir de los datos ingresados en la
  vista de crear producto.
  """
  if 'usuario' not in session:
    return redirect('/usuario/ingresar')
    
  product_form = ProductForm(request.form)

  if request.method == 'GET':
    return render_template('CrearProducto/crear_producto.html', form=product_form)
  
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

def comprar(id):
  """
  Compra un producto.
  Parámetros:
    id -- El identificador del producto a comprar.
  """
  product = Producto.query.get_or_404(id)
  usuario_login = Usuario.query.filter_by(usuario=session["usuario"]).first()
  correo = usuario_login.correo
  msg = Message('MercaTodo: Correo de confirmación',
                sender='corgitech2021@gmail.com',
                recipients=[usuario_login.correo])
  msg.body =  'Gracias por su compra en MercaTodo.\nPuede ver los detalles de su compra escaneando el codigo QR adjunto'

  with app.open_resource("qrcode.png") as fp:
    msg.attach("qrcode.png", "image/png", fp.read())
  try:
    mail.send(msg)
  except:
    raise abort(500, 'Ocurrió un error al intentar enviar correo de compra al usuario. Intente hacer nuevamente su compra')

  return render_template('comprar.html', correo=correo, name=session["usuario"])

def consultar():
  """
  Consulta la información de un producto.
  Encuentra todas las coincidencias en nombre, descripción y palabras relacionadas del producto.
  """
  searchword = request.args.get('q')
  products = Producto.query.msearch(searchword, fields=['nombre','descripcion','palabras_clave'], limit=3)

  return render_template('consulta.html', products=products, name=session["usuario"])

def masVendidos():
  """Página con los productos más vendidos"""
  consulta = Producto.query.order_by(Producto.cantidad_vendidos.desc())

  return render_template('masVendidos.html', consulta=consulta, name=session["usuario"])

def single_page(id):
  product = Producto.query.get_or_404(id)

  return render_template('single_page.html', product=product, name=session["usuario"])

'''def checkout(id):
  product = Producto.query.get_or_404(id)

  product.cantidad_vendidos += 1
  db.session.merge(product)
  db.session.commit()

  usuario_login = Usuario.query.filter_by(usuario=session["usuario"]).first()
  correo = usuario_login.correo
  compra = 'DETALLES DE COMPRA\n' + 'Cliente: ' + str(session["usuario"]) + '\nProducto: ' + str(product.nombre) + '\nDescripcion: ' + str(product.descripcion) + '\nPrecio: $' + str(product.precio)
  qr = qrcode.QRCode(version=1, box_size=10, border=5)

  qr.add_data(compra)
  qr.make(fit=True)

  img = qr.make_image(fill='black', black_color='white')
  img.save('controlador/qrcode.png')
  return render_template('checkout.html', product=product, correo=correo, name=session["usuario"])'''

def checkout(id):
  product = Producto.query.get_or_404(id)
  usuario_login = Usuario.query.filter_by(usuario = session["usuario"]).first()
  correo = usuario_login.correo
  c_form = CForm(request.form)
  if request.method == 'POST' and c_form.validate():
    product.cantidad_vendidos += 1
    db.session.merge(product)
    db.session.commit()
    usuario_login = Usuario.query.filter_by(usuario = session["usuario"]).first()
    correo = usuario_login.correo
    compra = 'DETALLES DE COMPRA\n' + 'Cliente: ' + str(session["usuario"]) + '\nProducto: ' + str(product.nombre) + '\nDescripcion: ' + str(product.descripcion) + '\nPrecio: $' + str(product.precio)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(compra)
    qr.make(fit=True)
    img = qr.make_image(fill='black', black_color='white')
    img.save('controlador/qrcode.png')
    print("QR generado")
    flash('Gracias por su compra')
    #return redirect(url_for('producto_bp.comprar'))
    return redirect('/producto/product/'+str(id)+'/checkout/comprar')
  else:
    return render_template('Checkout/checkout.html', form = c_form, product=product, correo=correo)


def catalogo():
  """Página con el catálogo de productos"""
  return render_template('catalogo.html', productos=Producto.query.all(), name=session["usuario"])


def index():
  """Página principal de Mis Publicaciones.

  Se pueden recibir peticiones para eliminar o actualizar.
  """
  if 'usuario' not in session:
    return redirect('/usuario/ingresar')

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

  # Se obtienen todos los productos que el usuario ha creado.
  productos_id = list(map(lambda x: x.id_producto,
                      Crear.query.filter_by(usuario=session['usuario']).all()))
  productos = [Producto.query.filter_by(id=id).first() for id in productos_id]

  return render_template('MisProductos/misPublicaciones.html', title='Mis Publicaciones', 
                          productos=productos, name=session['usuario'])
