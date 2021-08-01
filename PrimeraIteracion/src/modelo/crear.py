from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Crear(db.Model):
  __tablename__ = 'crear'

  usuario = db.Column(db.Unicode, primary_key=True)
  id_producto = db.Column(db.Integer, primary_key=True)

  def __init__(self, usuario, id_producto):
    """Crea un nuevo producto"""
    self.usuario = usuario
    self.id_producto = id_producto
