#Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.
lista = [0,0,0,0,0,0,0,0]
mayor = 0
menor = 0
print("A continuacion se creara una lista de 8 enteros")
for f in range (len(lista)):
    lista[f] = int(input("Ingresa un valor entero: "))
    if lista[f] >= 100:
        mayor = mayor + 1
    else:
        menor = menor + 1
print("Los numeros son los siguientes: ", lista)
print("La cantidad de numeros mayores a 100 son: ", mayor)
print("La cantidad de numeros menores a 100 son: ", menor)