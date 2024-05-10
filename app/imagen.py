from flask import Flask, render_template, request
from config import Conexion
from bson import ObjectId
import base64

app = Flask(__name__)

con_bd = Conexion()
users = con_bd['users']

@app.route('/')
def index():
    correo_acceso = 'nocua68@gmail.com'
    usuario = users.find_one({'correo': correo_acceso})
    imagen = usuario.get('image', None)
    imagen_base64 = base64.b64encode(imagen).decode('utf-8') if imagen else None
    return render_template('img.html', imagen_base64=imagen_base64)

@app.route('/upload', methods=['POST'])
def upload():
    correo_acceso = 'nocua68@gmail.com'
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Guarda la imagen en el usuario en MongoDB
            users.update_one({'correo': correo_acceso}, {'$set': {'image': image.read()}})
    return index()  # Renderiza la plantilla 'img.html' nuevamente después de cargar la imagen

if __name__ == '__main__':
    app.run(debug=True)
