import re
from flask_mail import Message
from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField


from wtforms import validators

class CommentForm(Form):
    usuario = StringField('Nombre de usuario:',
            [
                validators.Required(message = "El nombre de usuario es requerido."),
                validators.length(min=5, max=20, message='Ingrese un nombre de usuario válido. Son requeridos mínimo 5 caracteres y máximo 20.')
                
            ]
            )
    correo = EmailField('Correo:',
            [
                validators.Required(message = 'El correo es requerido.'),
                validators.Email(message='Ingrese un correo válido.')
            ]
            )
    telefono = StringField('Teléfono:',
            [
                validators.Required(message = "El teléfono es requerido."),
                validators.Regexp('^\d', message="Este campo solo debe contener números."),
                validators.length(min=10, max=10, message='Ingrese un teléfono válido. Son requeridos 10 números.')
            ]
            )
    