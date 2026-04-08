# class Usuario:      #molde



#     pass




# #Crear objetos (instancias)
# u1 = Usuario()  #instancias
# u2 = Usuario()

# # u1, u2 son objetos distintos
# # creados desde la misma clase


# #Atributos




class Usuario:
    def __init__(self, nombre,  edad,  email, activo ):

        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.activo = activo


u1 = Usuario("Josue", "penroz@gmail.com", 17 , True,)
u2 = Usuario("karen", "karen@gmail.com", 20, False)

print(u1.nombre)
print(u1.edad)
print(u1.email)
print(u1.activo)
print(u2.nombre)
print(u2.edad)
print(u2.email)
print(u2.activo)
