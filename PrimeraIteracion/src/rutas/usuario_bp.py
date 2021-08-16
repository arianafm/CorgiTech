from flask import Blueprint
from controlador.usuario_controlador import registrar, login, correo_confirmacion, logout, inicio

usuario_bp = Blueprint('usuario_bp', __name__)

"""
Rutas relacionadas a un usuario
- Registrar un usuario
- Dar ingreso a un usuario
- Enviar correo de confirmación
- Cerrar sesión de un usuario
- Inicio de sesión del usuario
"""
usuario_bp.route('/registrar', methods=['GET','POST'])(registrar)
usuario_bp.route('/ingresar', methods=['GET','POST'])(login)
usuario_bp.route('/enviar')(correo_confirmacion)
usuario_bp.route('/cerrar')(logout)
usuario_bp.route('/inicio', methods=['GET','POST'])(inicio)
