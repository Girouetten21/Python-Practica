"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.
"""

oracion = input("Ingresar una oracion: ")
oracionMin = oracion.lower()
cantidad = 0
w = 0

while w<len(oracionMin):
    if oracionMin[w] == "a" or oracionMin[w] == "e" or oracionMin[w] == "i" or  oracionMin[w] == "o" or oracionMin[w] == "u":
        cantidad = cantidad + 1
    w = w + 1
print("La cantidad de vocales en la oracion es: ", cantidad)
