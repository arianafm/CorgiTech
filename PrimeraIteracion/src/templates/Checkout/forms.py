import re
from flask_mail import Message
from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import IntegerField

from wtforms import validators

class CForm(Form):
    nombres = StringField('Nombre(s)',
            [
                validators.DataRequired(message = "El nombre es requerido."),                
            ]
            )

    apellidos = StringField('Apellidos',
            [
                validators.DataRequired(message = "Los apellidos son requeridos."),                
            ]
            )

    direccion = StringField('Dirección',
            [
                validators.DataRequired(message = "La dirección es requerida."),                
            ]
            )
    
    cp = IntegerField('CP',
            [
                validators.NumberRange(min=0, message="El CP no puede ser negativo"),
                validators.DataRequired(message = "El código postal es requerido.")
            ]
            )