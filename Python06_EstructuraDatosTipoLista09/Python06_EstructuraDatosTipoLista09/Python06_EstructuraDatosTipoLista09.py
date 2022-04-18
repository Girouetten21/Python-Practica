#Imprimir la lista: [4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]
#Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
#Volver a imprimir la lista.

lista = [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
print("Lista: ", lista)
for f1 in range(len(lista[0])):
    for f2 in range(len(lista[f1])):
        if lista[f1][f2] > 10:
            lista[f1][f2] = 0
print("Lista: ", lista)