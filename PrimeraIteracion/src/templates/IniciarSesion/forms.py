import re
from flask_mail import Message
from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField


from wtforms import validators

class LoginForm(Form):
    usuario = StringField('Nombre de usuario:',
            [
                validators.Required(message = "El nombre de usuario es requerido."),
                validators.length(min=5, max=20, message='Ingrese un nombre de usuario válido.')
                
            ]
            )
    contrasena = StringField('Contraseña:',
            [
                validators.Required(message = "La contraseña es requerida."),
                validators.length(min=10, max=10, message='Ingrese una contraseña válida.')
                
            ]
            )
    