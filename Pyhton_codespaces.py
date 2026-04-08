#Herencia 
class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.activo = True
    def login(self, nombre, nontraseña):
        self.activo = True
        return f"{self.nombre} Esta logeado" 
    def logout(self):
        self.activo = False
        return f"{self.nombre} se ha deslogeado"
class Admin