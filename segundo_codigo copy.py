num = 6 

if num > 5 :
    print("EL NÚMERO ES MAYOR QUE 5")
    print("Esto tambien forma parte del bloque")

print("Esto ")



MENSAJE = "Hola mundo"

NOMBRE = "Josue"

print("Me llamo", NOMBRE) #Cuando usas la coma no es necesario agregar un espacio

print("Mi nombre es " + NOMBRE) #agregar un espacio cuando usamos el +

print(NOMBRE+"gmail.com")
print("mi edad es" , str(17) , "😊")



# forma mas usada
ESTUDIANTE = "Esteban"
EDAD  = 17
print("---------------------------------------------------")
print(f"Mi nombre es {ESTUDIANTE} y tengo {EDAD} años")


# format()


#A diferencia de otros lenguajes, las listas en Python pueden tener distintos tipos de datos, cadenas, números, inclusive otras listas o tuplas.


print("Mi nombre es {} y tengo {} años" .format(ESTUDIANTE,EDAD))

lista_vacia = []
print('--------------------------------------------------------------------------' )
lista_compras = ['tomate', "pan", "queso" , "jamon"]

lista_especial = [1, 2, ['a', 'b', 'c'], True]

lista_colegio=["lapices","cuadernos","libretas"]
lista_compras1=["pasta de dientes", "lechuga", lista_colegio]

print(lista_compras1)
lista_colegio[2]= "block"
lista_colegio[2]= "block"
print(lista_compras1)
print("-----------------------------------------------")
cajonera=["pantalon","camisetas", "calcetines"]
print(cajonera[0])
print(cajonera[1])
print(cajonera[2])
cajonera[1] = "sueter"

print(cajonera[1])

cajonera.append("ropa interior")

print(cajonera)




PALABRA = input("Escribe una palabra: ")

print("Mayuscula:", PALABRA.upper())
print("Minuscula:", PALABRA.lower())
print(" Cantidad de letras:", len(PALABRA))