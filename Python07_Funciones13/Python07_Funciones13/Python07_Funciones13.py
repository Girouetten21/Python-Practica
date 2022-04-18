"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def cargar_datos():
    l = []
    for f in range (10):
        v = int(input("Ingresar valores: "))
        l.append(v)
    return l

def positivo_negativo(lista):
    l1 = []
    l2 = []
    for f in range (len(lista)):
        if lista[f] >= 0:
            l1.append(lista[f])
        else:
            l2.append(lista[f])
    print("Lista positiva: ", l1)
    print("Lista negativa: ", l2)
###START
lista = cargar_datos()
positivo_negativo(lista)
