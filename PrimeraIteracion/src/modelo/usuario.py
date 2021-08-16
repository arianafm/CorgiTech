from modelo._db import db
import controlador.usuario_controlador

class Usuario(db.Model):
  """Clase para los usuarios."""
  __tablename__ = 'usuario'

  usuario = db.Column(db.Unicode, primary_key=True)
  correo = db.Column(db.Unicode, unique=True)
  telefono = db.Column(db.Unicode)
  contrasena = db.Column(db.Unicode)

  def __init__(self, usuario, correo, telefono):
    """"
    Crea un nuevo usuario.
    Parámetros:
      usuario -- nombre de usuario del usuario a crear
      correo -- correro asociado al usuario
      telefono -- numero de teléfono del usuario
    """
    self.usuario    = usuario
    self.correo     = correo
    self.telefono   = telefono
    self.contrasena = controlador.usuario_controlador.generar_contrasena()
