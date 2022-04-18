#Cargar una lista con 5 elementos enteros. 
#Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
valor = 0
lista=[]
numMayor = 0
numRepetido = 0
for f in range(5):
    valor = int(input("Ingresar valor entero: "))
    lista.append(valor)
    if lista[f] > numMayor:
        numMayor = lista[f]
    if lista[f] == numMayor:
        numRepetido = numRepetido + 1
print("Lista: ", lista)
print("Numero mayor: ", numMayor)
print("Cantidad de veces que se repitio en la lista: ", numRepetido)