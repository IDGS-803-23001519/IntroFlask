from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UseForm(Form):
    matricula=IntegerField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=2,max=100,message='ingresa valor valido')
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingresae nombre valido')])
    apaterno=StringField('Apaterno',[
        validators.DataRequired(message='El campo es requerido')])
    amaterno=StringField('Amaterno',[
        validators.DataRequired(message='El campo es requerido')])
    email=EmailField('Correo',[
        validators.Email(message='Ingrese un correo valido')
    ])
    
    