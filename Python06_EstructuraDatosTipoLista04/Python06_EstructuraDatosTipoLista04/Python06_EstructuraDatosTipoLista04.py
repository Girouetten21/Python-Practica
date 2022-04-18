#Almacenar en una lista los sueldos (valores float) de 5 operarios. 
#Imprimir la lista y el promedio de sueldos.
valor = 0
lista=[]
listaSuma = 0
for f in range(5):
    valor=float(input("Ingresa sueldo: "))
    lista.append(valor)
    listaSuma = listaSuma + lista[f]
print("Lista de sueldos: ", lista)
print("Promedio: ", listaSuma / 5)