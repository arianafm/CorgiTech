from flask import Blueprint
from controlador.usuario_controlador import index, registrar, login, correo_confirmacion, logout

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/', methods=['GET'])(index)
usuario_bp.route('/registrar', methods=['GET','POST'])(registrar)
usuario_bp.route('/ingresar', methods=['POST'])(login)
usuario_bp.route('/enviar')(correo_confirmacion)
usuario_bp.route('/cerrar')(logout)

