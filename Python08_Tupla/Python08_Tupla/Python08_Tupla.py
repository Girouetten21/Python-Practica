"""
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.

"""
def cargar_datos():
    lista = []
    for f in range (5):
        valor = int(input("Ingresar valores: "))
        lista.append(valor)
    listaTupla = tuple(lista)
    return listaTupla
def mayor_menor(litu):
    mayor = 0
    menor = 0
    li = list(litu)
    for f in range(1,len(li)):
        if li[mayor] < li[f]:
            mayor = f
        if li[menor] > li[f]:
            menor = f
    print("Mayor", li[mayor])
    print("Menor", li[menor])
###START
l = cargar_datos()
mayor_menor(l)
