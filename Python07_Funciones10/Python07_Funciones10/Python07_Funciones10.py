#Definir una lista de enteros por asignación en el bloque principal. 
#Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
#Mostrar dicho producto en el bloque principal de nuestro programa.
def return_producto(lista):
    producto = lista[0]
    for f in range (1,len(lista)):
        producto = producto * lista[f]
    return producto
###START
lista1 = [5,10,15,20,25]
print("Lista: ", lista1)
print("Producto de la lista: ", return_producto(lista1))