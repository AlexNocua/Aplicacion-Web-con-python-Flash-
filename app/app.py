# # save this as app.py
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World sou alex!"
#####################################
# inicializacion base
#####################################

from flask import Flask, render_template, request , redirect,url_for
from config import *
from ClaseFormulario import formulario


con_bd =conexion()

# definicion de archivo principal
app = Flask(__name__)


@app.route('/')
def login():
    # rednerizado con jinja2
    return render_template('login.html')

# prueba de funcionamiento y rendereizado de la pagina principal


@app.route('/pagina_principal')
def pagina_principla():
    return render_template('pagina_principal.html')


@app.route('/publicacion')
def agregarUser():
    return render_template('publicacion.html')


@app.route('/personInformation')
def inforPerson():
    return render_template('informacionPersona.html')


@app.route('/registro') 
def index():  
    coleccionPersonas =con_bd['Registro']
    PersonasRegistradas = coleccionPersonas.find()
    return render_template('login.html', datos = PersonasRegistradas)


@app.route('/guardar_personas',methods=['POST']) 
def agregarPersona():
    personas =con_bd['personas']
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    residencia = request.form['residencia']
    contraseña = request.form['contraseña']
    configContraseña= request.form['configContraseña']


    if nombre and usuario and residencia and contraseña and configContraseña: 
        persona1 = formulario(nombre,residencia,contraseña,configContraseña)
        personas.insert_one(persona1.formato_doc())
        return redirect(url_for('index'))
    
    else:
        return "Error "

if __name__ == '__main__':
    app.run(debug=True)
