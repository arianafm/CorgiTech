import os

# Configuración del servidor.

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Conexión a la base de datos.
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/mercatodo'

# Configuración del correo
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'corgitech2021@gmail.com'
MAIL_PASSWORD = 'fbgfqabyxaijedkf'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
