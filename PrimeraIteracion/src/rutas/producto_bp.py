from itertools import product
from flask import Blueprint
from controlador.producto_controlador import index, crear, catalogo, single_page, checkout, comprar, consultar

producto_bp = Blueprint('producto_bp', __name__)

producto_bp.route('/', methods=['GET', 'POST'])(index)
producto_bp.route('/crear', methods=['GET', 'POST'])(crear)
producto_bp.route('/catalogo', methods=['GET', 'POST'])(catalogo)
producto_bp.route('/consultar', methods=['GET','POST'])(consultar)
producto_bp.route('/product/<int:id>', methods=['GET'])(single_page)
producto_bp.route('/product/<int:id>/checkout', methods=['GET'])(checkout)
producto_bp.route('/product/<int:id>/checkout/comprar', methods=['GET', 'POST'])(comprar)