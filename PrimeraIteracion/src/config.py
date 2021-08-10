import os

# Configuración del servidor.

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Conexión a la base de datos.
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/mercatodo'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
