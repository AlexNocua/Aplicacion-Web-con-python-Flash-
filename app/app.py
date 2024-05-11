
from flask import Flask, render_template, request, redirect, url_for
from config import *
from ClaseFormulario import formulario
import base64


# con_bd = conexion() #Baquero
con_bd = Conexion()  # alex

app = Flask(__name__)


@app.route('/')
def login():
    # rednerizado con jinja2
    coleccionPersonas = con_bd['users']
    PersonasRegistradas = coleccionPersonas.find()
    return render_template('login.html', datos=PersonasRegistradas)


@app.route('/guardar_registro', methods=['POST'])
def agregarPersona():
    personas = con_bd['users']
    # personas =con_bd['Registro'] Baquero
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    configContraseña = request.form['configContraseña']

    if nombre and apellido and correo and contraseña and configContraseña:
        persona1 = formulario(nombre, apellido, correo,
                              contraseña, configContraseña, None)
        personas.insert_one(persona1.formato_doc())
        return redirect(url_for('login'))

    else:
        return "Error "

# prueba de funcionamiento y rendereizado de la pagina principal

# logica de inicio de sesion


@app.route('/iniciarSesion', methods=['post'])
def iniciarSesion():
    users = con_bd['users']
    correo_acceso = request.form['Email_de_acceso']
    contraseña_acceso = request.form['Contraseña_de_acceso']

    # verificar si se puede implementar mas condiciones respecto a ello
    # print('datos dek ususario depuesdel envio de la imagen', datos_usuario)
    usuario_Existente = users.find_one(
        {'correo': correo_acceso, 'contraseña': contraseña_acceso})
    if usuario_Existente:
        nombre, apellido, correo, imagen = usuario_Existente['nombre'], usuario_Existente[
            'apellido'], usuario_Existente['correo'], usuario_Existente['image']

        # print(imagen, 'fffffffffffffffffffffffffffffffffffffff')
        imagen_base64 = base64.b64encode(
            imagen).decode('utf-8') if imagen else None

        # imagen_base64 = request.args.get('imagen_base64', None)
        # print('existe' if imagen_base64 else 'no existe')

        return index(usuario_Existente, imagen_base64)
    else:
        return 'No existe el usuario'


# logica para editar los datos del ussuario desde la configuracion
@ app.route('/principal')
def index(usuario_Existente, imagen_base64):
    users = con_bd['users']
    correo_acceso = usuario_Existente['correo']
    usuario = users.find_one({'correo': correo_acceso})
    imagen = usuario.get('image', None)
    imagen_base64 = base64.b64encode(
        imagen).decode('utf-8') if imagen else None

    return render_template('pagina_principal.html', datos_usuario=usuario_Existente, imagen_base64=imagen_base64)


@ app.route('/upload', methods=['POST'])
def upload():

    datos_usuario = request.args.get('datos_usuario')
    users = con_bd['users']
    correo_acceso = 'nocua68@gmail.com'
    print(datos_usuario, ' estos son los datos del usuario')
    if 'imagen' in request.files:

        imagen = request.files['imagen']
        users.update_one({'correo': correo_acceso}, {
            '$set': {'image': imagen.read()}})
        return 'Imagen subida'

    return 'No se ha proporcionado ninguna imagen'

# @app.route('/Cargarimagen/<correo>', methods=['POST'])
# def upload(correo):
#     users = con_bd['users']
#     correo_acceso = correo
#     if 'image' in request.files:
#         image = request.files['image']
#         if image.filename != '':
#             # Guarda la imagen en el usuario en MongoDB
#             users.update_one({'correo': correo_acceso}, {
#                              '$set': {'image': image.read()}})
#     # Redirige de vuelta a la página principal o a donde quieras después de cargar la imagen
#     return redirect(url_for('principal'))


# logica para cargar la publicacion de cada uno de los estudiantes

@app.route('/subirPublicacion', method='POST')
def subirPublicacion():
    publicaciones = con_bd['publicaciones']
    usuario = request.form['correo']
    
    


@ app.route('/pagina_principal')
def pagina_principla(datos_usuario):

    return render_template('pagina_principal.html', datos_usuario=datos_usuario)


@ app.route('/publicacion')
def agregarUser():
    return render_template('publicacion.html')


@ app.route('/personInformation')
def inforPerson():
    return render_template('informacionPersona.html')

# modulo de configuraciones


@ app.route('/configuracion')
def configuracion():
    return render_template('configuracionCuenta.html')


if __name__ == '__main__':
    app.run(debug=True)
