#Herencia Render Whitespace
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

class Admin(Usuario):
    def __init__(self,nombre, contraseña, nivel_acceso="parcial"):
        super().__init__(nombre, contraseña)
        self.nivel_acceso = nivel_acceso
    
    def Eliminar_user(self, user):
        return f"{self.nombre} ha eliminado al {user.nombre}"
    
    def login(self):
        super().login()
        return f"Ha ingresada el usuario {self.nombre}, administrador con nivel de acceso {self.nivel_acceso}"




class Influencer(Usuario):
    def __init__(self, nombre, contraseña, seguidores):
        super().__init__(nombre, contraseña)
        self.seguidores = seguidores
    def publicar(self, post):
        return f"{self.nombre} a publicado un {post}"
    
danirep = Influencer("danirep", "212121", 9000)

print(danirep.publicar("Aparentemente"))
print(f"danirep tiene {danirep.seguidores} ahora")

class seguidor(Usuario):
    def __init__(self, nombre, contraseña, seguidor):
        super().__init__(nombre, contraseña)
        self.seguidor = seguidor
    def revisar(self, like):
        return f"{self.nombre} a dado like a {like}"
josue = seguidor("josue","1012", "dio 12 like")

print(josue.revisar("ultima destacada"))
print(f"josue reviso {self.publicar} de danirep")