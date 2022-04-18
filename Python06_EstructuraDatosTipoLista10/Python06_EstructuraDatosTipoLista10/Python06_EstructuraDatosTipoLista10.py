##Solicitar por teclado dos enteros. 
#El primer valor indica la cantidad de elementos que crearemos en la lista. 
#El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
#Mostrar la lista y la suma de todos sus elementos.

filas = int(input("Ingresa cantidad de filas: "))
columnas = int(input("Ingresa cantidad de columnas: "))
lista = []
for fi in range (filas):
    lista.append([])
    for co in range (columnas):
        colum = int(input("Ingresar numero para la lista: "))
        lista[fi].append(colum)
print(lista)
suma=0
for fi in range(len(lista)):
    for co in range(len(lista[fi])):
        suma=suma+lista[fi][co]
print(suma)