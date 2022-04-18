#Crear una lista de enteros por asignación.
#Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. 
#Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
def return_lista(lista,mult):
    listamulti = []
    for f in range(len(lista)):
        valor = lista[f] * mult
        listamulti.append(valor)
    return listamulti
###START
lista1 = [1,5,10,15,20,25]
mult1 = int(input("Ingresar multiplicador: "))
print("Lista normal: ", lista1)
print("Multiplicada: ", return_lista(lista1,mult1))