import re
from flask_mail import Message
from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import IntegerField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class ProductForm(Form):
    nombre = StringField('Nombre de producto:',
            [
                validators.Required(message = "El nombre de producto es requerido."),                
            ]
            )
    descripcion = StringField('Descripción de producto:',
            [
                validators.Required(message = "La descripción de producto requerida."),
            ]
            )
    imagen = StringField('Fotografía del producto:',
            [
                validators.Required(message= "La fotografría del producto es requerida"),
            ]
            )
    precio = IntegerField('Precio del producto:',
            validators=[
                validators.NumberRange(min=1),
                validators.Required(message = "El precio del producto es requerido.")
            ])
    palabras_clave = StringField('Palabras relacionadas:',
            [
                validators.Required("Las palabras relacionada son requeridas.")
            ])