from flask import Blueprint
from controlador.usuario_controlador import index, registrar

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/', methods=['GET'])(index)
usuario_bp.route('/registrar', methods=['POST'])(registrar)

