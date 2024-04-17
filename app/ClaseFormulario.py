class formulario:
    def __init__(self,nombre,usuario,residencia,contraseña,configContraseña):
        self.nombre = nombre
        self.usuario = usuario
        self.residencia = residencia
        self.contraseña = contraseña
        self.configContraseña = configContraseña
       


    def formato_doc(self):
        return{
            'nombre': self.nombre,
            'usuario': self.usuario,
            'residencia': self.residencia,
            'contraseña': self.contraseña,
            'configContraseña': self.configContraseña
    
        }   

