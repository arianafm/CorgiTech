from modelo._db import db
import controlador.usuario_controlador


class Usuario(db.Model):
  __tablename__ = 'usuario'

  usuario = db.Column(db.Unicode, primary_key=True)
  correo = db.Column(db.Unicode, unique=True)
  telefono = db.Column(db.Unicode)
  contrasena = db.Column(db.Unicode)

  def __init__(self, usuario, correo, telefono):
    self.usuario    = usuario
    self.correo     = correo
    self.telefono   = telefono
    self.contrasena = controlador.usuario_controlador.generar_contrasena()
