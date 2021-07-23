from flask import Blueprint
from controlador.producto_controlador import index, crear, eliminar, actualizar

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET'])(index)
producto_bp.route('/crear', methods=['POST'])(crear)
producto_bp.route('/eliminar', methods=['DELETE'])(eliminar)
producto_bp.route('/actualizar', methods=['POST'])(actualizar)