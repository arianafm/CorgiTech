from flask import Blueprint
from controlador.producto_controlador import index, crear, actualizar

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET', 'POST'])(index)
producto_bp.route('/crear', methods=['POST'])(crear)
producto_bp.route('/actualizar', methods=['POST'])(actualizar)