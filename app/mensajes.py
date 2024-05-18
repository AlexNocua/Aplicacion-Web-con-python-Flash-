from datetime import *


class Mensajes:
    def __init__(self, usuario1, usuario2, mensajes=None):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.mensajes = mensajes
        self.fechas = datetime.now().strftime(
            "Chat creado en la fecha %Y-%m-%d  y en el tiempo %H:%M:%S")

    def formato_doc(self):
        return {
            'usuario1': self.usuario1,
            'usuario2': self.usuario2,
            'mensajes': self.mensajes,
            'fechas': self.fechas
        }
