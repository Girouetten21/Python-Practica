#Crear una lista de 5 enteros y cargarlos por teclado. 
#Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
lista1 = []
lista2 = []
pos = 0
for x in range(5):
    valor = int(input("Ingrese valor:"))
    lista1.append(valor)
print("Lista original")
print(lista1)
while pos < len(lista1):
    if lista1[pos] >= 10:
        lista2.append(lista1.pop(pos))
    else:
        pos = pos + 1
print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)