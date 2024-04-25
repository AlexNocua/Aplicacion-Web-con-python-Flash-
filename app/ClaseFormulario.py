
class formulario:
    def __init__(self,nombre,apellido,correo,contraseña,configContraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.configContraseña = configContraseña
    
    def formato_doc(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'contraseña': self.contraseña,
            'configContraseña': self.configContraseña
    
        }   

