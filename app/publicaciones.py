from datetime import *


class Publicacion:
    def __init__(self, correo_user, nombre_user, publicacion_text, publicacion_img=None):
        self.nombre_user = nombre_user
        self.correo_user = correo_user
        self.publicacion_text = publicacion_text
        self.publicacion_img = publicacion_img
        self.fecha_publicacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formato_doc(self):
        return {
            'correo_user': self.correo_user,
            'nombre_user': self.nombre_user,
            'publicacion_text': self.publicacion_text,
            'publicacion_img': self.publicacion_img,
            'fecha_publicacion': self.fecha_publicacion
        }


p = Publicacion('aaa', 'dasdas', 'asdasdas', None)
print(p)
print(p.formato_doc())
