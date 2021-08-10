from modelo._db import db

from flask_msearch import Search

search = Search(db=db)

class Producto(db.Model):
  """Clase para los productos.

  Automáticamente se le asigna un id de acuerdo a la base de datos.
  """
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
    """Crea un nuevo producto."""
    self.nombre = nombre
    self.descripcion = descripcion
    self.imagen = imagen
    self.precio = precio
    self.palabras_clave = palabras_clave
    self.cantidad_vendidos = 0
