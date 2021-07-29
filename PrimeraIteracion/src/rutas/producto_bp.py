from itertools import product
from flask import Blueprint
from controlador.producto_controlador import index, agregar, eliminar, create_product

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET'])(index)
producto_bp.route('/agregar')(agregar)
producto_bp.route('/eliminar', methods=['DELETE'])(eliminar)
producto_bp.route('/agregar', methods=['POST'])(create_product)