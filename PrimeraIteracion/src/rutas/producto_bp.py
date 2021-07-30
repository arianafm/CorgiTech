from itertools import product
from flask import Blueprint
from controlador.producto_controlador import index, crear, actualizar, create_product

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET', 'POST'])(index)
producto_bp.route('/crear')(crear)
producto_bp.route('/actualizar', methods=['POST'])(actualizar)
producto_bp.route('/crear', methods=['POST'])(create_product)
