import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'mysql://root:Cesar143$@localhost/mercatodo'
=======
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/mercatodo'
>>>>>>> 4b103a2165f5c1c359e075293c1f16e6b1694fd6

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False