from flask import Flask, render_template, request , redirect,url_for
from config import *
from ClaseFormulario import formulario



app = Flask(__name__)

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
