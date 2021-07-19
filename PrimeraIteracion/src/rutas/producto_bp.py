from flask import Blueprint
from controlador.producto_controlador import index, agregar, eliminar

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET'])(index)
producto_bp.route('/agregar', methods=['POST'])(agregar)
producto_bp.route('/eliminar', methods=['DELETE'])(eliminar)
