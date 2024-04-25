
from flask import Flask, render_template, request , redirect,url_for
from config import *
from ClaseFormulario import formulario


con_bd =conexion()

# definicion de archivo principal
app = Flask(__name__)


@app.route('/')
def login():
    # rednerizado con jinja2
    coleccionPersonas =con_bd['Registro']
    PersonasRegistradas = coleccionPersonas.find()
    return render_template('login.html', datos = PersonasRegistradas)

@app.route('/guardar_registro',methods=['POST']) 
def agregarPersona():
    personas =con_bd['Registro']
    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    configContraseña = request.form['configContraseña']

    if nombre and apellido and correo and contraseña and configContraseña : 
        persona1 = formulario(nombre,apellido,correo,contraseña,configContraseña)
        personas.insert_one(persona1.formato_doc())
        return redirect(url_for('login'))
    
    else:
        return "Error "
    
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


   
if __name__ == '__main__':
    app.run(debug=True)
