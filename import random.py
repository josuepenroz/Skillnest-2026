import random

print("numero random:")
print(random.randint(1, 6))

numero_decimal = 10.5

entero = int(numero_decimal)
print(entero)

cadena = "100"
numero_entero = int(cadena)
print(type(numero_entero))

try: valor = int("abc")
except ValueError:
    print("No se pudo convertir a entero")