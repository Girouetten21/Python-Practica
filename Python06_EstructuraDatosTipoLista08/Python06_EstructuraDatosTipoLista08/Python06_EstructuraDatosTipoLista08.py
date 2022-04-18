#Imprimir la lista: [100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]
#Luego fijar con el valor cero todos los elementos mayores a 50 de la lista.
#Volver a imprimir la lista.

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print("Lista: ", lista)
for f1 in range(len(lista[0])):
    for f2 in range(len(lista[f1])):
        if lista[f1][f2] > 50:
            lista[f1][f2] = 0
print("Lista actualizada: ", lista)

