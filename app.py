from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms
from forms import CinepolisForm

app = Flask(__name__)
app.secret_key='clave secreta'
csrf=CSRFProtect()


@app.route("/index")
def index():
    titulo="IDGS803-Flask"
    lista=['Pedro','mario','juan']
    return render_template('index.html',titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template('alumnos.html')

@app.route("/usuario",methods=["GET", "POST"])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    correo=''
    usuario_class=forms.UseForm(request.form)
    if request.method=='POST' and usuario_class.validate():
        mat=usuario_class.matricula.data
        nom=usuario_class.nombre.data
        apa=usuario_class.apaterno.data
        ama=usuario_class.amaterno.data
        correo=usuario_class.email.data

    return render_template('usuario.html',form=usuario_class,mat=mat,nom=nom,
                           apa=apa,ama=ama,correo=correo)

@app.route('/hola')
def hola():
    return "Hello, Hola!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>!Hola, {username}! Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1>!Hola, {param}!<h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>
            '''

@app.route("/operaBas",methods=["GET", "POST"])
def operas1():
    resultado=0
    if request.method == 'POST':
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = n1 + n2
            op = "suma"

        elif operacion == "resta":
            resultado = n1 - n2
            op = "resta"

        elif operacion == "multiplicacion":
            resultado = n1 * n2
            op = "multiplicación"

        elif operacion == "division":
            if n2 == 0:
                return "<h1>Entre 0 no</h1>"
            resultado = n1 / n2
            op = "división"
        
    return render_template('operaBas.html',resultado=resultado)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    operacion = request.form.get("operacion")

    if operacion == "suma":
        resultado = n1 + n2
        op = "suma"

    elif operacion == "resta":
        resultado = n1 - n2
        op = "resta"

    elif operacion == "multiplicacion":
        resultado = n1 * n2
        op = "multiplicación"

    elif operacion == "division":
        if n2 == 0:
            return "<h1>Error: No se puede dividir entre 0</h1>"
        resultado = n1 / n2
        op = "división"

    return f"<h1>El resultado de la {op} es: {resultado}</h1>"


@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm(request.form)
    total_pagar = 0.0
    mensaje = ""

    if request.method == 'POST' and form.validate():
        try:
            nombre = form.nombre.data
            compradores = int(form.cant_compradores.data)
            boletas = int(form.cant_boletas.data)
            tarjeta = form.tarjeta.data
            
            max_boletas_permitidas = compradores * 7

            if boletas > max_boletas_permitidas:
                mensaje = f"Error: No se pueden comprar más de 7 boletas por persona. (Máximo permitido para {compradores} personas: {max_boletas_permitidas})"
            else:
                precio_unitario = 12.0
                total = boletas * precio_unitario

                if boletas > 5:
                    total = total * 0.85  
                elif boletas >= 3:
                    total = total * 0.90 

                if tarjeta == 'Si':
                    total = total * 0.90 
                
                total_pagar = total
                mensaje = f"Procesado exitosamente para {nombre}"

        except Exception as e:
            mensaje = "Ocurrió un error en el cálculo"

    return render_template("cinepolis.html", form=form, total=total_pagar, mensaje=mensaje)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)