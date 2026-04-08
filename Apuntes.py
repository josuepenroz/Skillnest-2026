EDAD = 1

if EDAD >= 18:
    print("puede comprar alcohol")


EDAD= 20 
TIENE_LICENCIA = True

if EDAD >= 18 and TIENE_LICENCIA:
    print("Puede conducir")

print("------------------------------------------------------------")

L = ["lo", "li", "le"]


L.insert(0, "le")

print(L)

print("-------------------------------------------------------------")

LISTA= [2,4,6,8,10,12]


print(LISTA[2:5])   #[6,8,10] agarra desde 2 al 4 porque 5 es el limite. Esto en indices. 
print(LISTA[:3])    #[2,4,6] agarra desde 0 hasta 2 y 3 es el limite. Esto en indices.




#Diccionarios:El diccionario en Python es una estructura de datos que nos permite almacenar contenido a través de una llave (o clave) y un valor, a estos pares les llamamos ítems o elementos


paises ={}
print(paises)

paises["CL"] = "Chile"
paises[ "MEX"] = "Mexico"
paises["COL"] = "Colombia"
paises["US"] = "Estados Unidos"
print(paises)

paises["MEX"]="Méjico"

print(paises)

lista_estudiantes=[
    {"nombre":"carolina", "curso": "python"}, #primer elemento
    {"nombre":"benjamin", "curso": "mern"},
    {"nombre":"sebastian", "curso": "fundamentos web"},
    {"nombre":"Bastian", "curso": "python"} #Ultimo elemento
]
print(lista_estudiantes)
lista_estudiantes[2]["Curso"]="Python"

print("-----------------------------------------")

#Lista: si se puede modificar
frutas = ["manzana", "pera", "naranja"]

frutas[0] = "kiwi"

#Tupla: no se puede modificar
frutas = ("manzana", "pera", "naranja")

print(frutas)

print("------------------------------------------")
#Colores del arcoíris en lista y tupla.

Colores = ["rojo","naranja","amarillo","verde","azul","añil","violeta"]

print(Colores)

print("primer color", Colores[0])
print("Ultimo color", Colores[6])
print("Cantidad de colores", len(Colores))

colores = ("rojo", "naranja", "amarillo", "verde", "azul", "añil", "violeta")

print(colores)
print("Primer color:", colores[0])
print("Último color:", colores[-1])

