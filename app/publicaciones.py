from datetime import *


class Publicacion:
    def __init__(self, nombre_user, publicacion_text, publicacion_img):
        self.nombre_user = nombre_user
        self.publicacion_text = publicacion_text
        self.publicacion_img = publicacion_img
        self.fecha_publicacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formato_doc(self):
        return {
            'nombre_user': self.nombre_user,
            'publicacion_text': self.publicacion_text,
            'publicacion_img': self.publicacion_img,
            'fecha_publicacion': self.fecha_publicacion
        }


p = Publicacion('Alex', 'hola todos', None)


# cuando quiera acceder a los metodos de la clase tengo que hacerlo desde la instancia
print(p.formato_doc())
