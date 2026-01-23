from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
def index():
    titulo="IDGS803-Flask"
    lista=['Pedro','mario','juan']
    return render_template('index.html',titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template('alumnos.html')

@app.route("/usuario")
def usuarios():
    return render_template('usuario.html')

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
@app.route("/default/string:parm>")
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

if __name__ == '__main__':
    app.run()
