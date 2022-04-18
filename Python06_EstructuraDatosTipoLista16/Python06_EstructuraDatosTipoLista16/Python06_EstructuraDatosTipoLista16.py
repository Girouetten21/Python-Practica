#Crear una lista y almacenar 10 enteros pedidos por teclado. 
#Eliminar todos los elementos que sean iguales al número entero 5.
lista = []
pos = 0
for f in range (10):
    valor = int(input("Ingresar un valor: "))
    lista.append(valor)
print("Lista completa: ", lista)
while pos < len(lista):
    if lista[pos] == 5:
        lista.pop(pos)
    else:
        pos = pos +1
print("Lista sin el numero 5: ", lista)