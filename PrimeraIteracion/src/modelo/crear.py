from modelo._db import db

class Crear(db.Model):
  """Clase para la relación usuario compra producto."""
  __tablename__ = 'crear'

  usuario = db.Column(db.Unicode, primary_key=True)
  id_producto = db.Column(db.Integer, primary_key=True)

  def __init__(self, usuario, id_producto):
    """Crea un nuevo producto"""
    self.usuario = usuario
    self.id_producto = id_producto
