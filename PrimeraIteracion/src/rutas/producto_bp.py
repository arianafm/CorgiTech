from itertools import product
from flask import Blueprint
from controlador.producto_controlador import index, crear

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET', 'POST'])(index)
producto_bp.route('/crear', methods=['GET', 'POST'])(crear)
