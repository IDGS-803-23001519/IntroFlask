from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField, RadioField, SubmitField
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

class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    cant_compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message="Debe haber al menos 1 comprador")
    ])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('Si', 'Si'), ('No', 'No')], default='No')
    cant_boletas = IntegerField('Cantidad de Boletas', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message="Debe comprar al menos 1 boleta")
    ])
    
    