from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from modelo.producto import db
from modelo.usuario import db
from rutas.producto_bp import producto_bp
from rutas.usuario_bp import usuario_bp


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
app.register_blueprint(producto_bp, url_prefix='/producto')
app.register_blueprint(usuario_bp, url_prefix='/usuario')

@app.route('/', methods=['GET'])
def index():
    # return render_template('index.html')
    return jsonify ({'msg': 'Pagina principal :D'})


if __name__ == '__main__':
    app.debug = True
    app.run()
