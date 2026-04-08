
print("argumento(fin)")
for i in range(4):
    print(i)
print("Argumentos (inicio,fin)") 
for i in range(2,8 ):
    print(i)

print("Argumentos ( inicio, fin, paso)") 
for i in range(2, 10, 3):
    print(i)


lista = ["lapiz", "papel","plumon"]

print("len(lista):")
print(len(lista))

ESTUDIANTES =  {"NOMBRE":"gonzalo","curso": "python" }
for clave in ESTUDIANTES:
    print(clave)
ESTUDIANTES =  {"NOMBRE":"gonzalo","curso": "python" }
for item in ESTUDIANTES:
    print(ESTUDIANTES[clave])
    print(ESTUDIANTES.keys())
    print(ESTUDIANTES.items())

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
platillos_tipicos = {  "Mexico": "Tacos", "colombis": "Ajiaco"}

for clave in platillos_tipicos.keys(): #Nos entra una claves
    print(clave)

for valor in platillos_tipicos.values(): #Nos entrega valor
    print(valor)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# while es un manera de crear un bucle esta va hacer repetida mientras sea verdadera 

while "condicion":

    NUM = 0
while NUM < 4:
    print("bucle while -", NUM)
    NUM += 1
else:
    print("Acabamos de salir del bucle")
