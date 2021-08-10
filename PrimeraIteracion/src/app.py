from flask import request, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_msearch import Search 
from flask_mail import Mail
from controlador.usuario_controlador import inicio

from modelo._db import db
from _app import app
from modelo.producto import search
from rutas.producto_bp import producto_bp
from rutas.usuario_bp import usuario_bp

db.init_app(app)
search.init_app(app)

# Registramos las rutas a usar.
app.register_blueprint(producto_bp, url_prefix='/producto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')

@app.errorhandler(404)
def page_not_found(e):
    """Método para manejar los errores de tipo 404."""
    return "404 D:"

@app.route('/', methods=['GET'])
def index():
    return inicio()

if __name__ == '__main__':
    app.debug = True
    app.run()
