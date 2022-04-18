"""
Definir dos listas de 3 elementos.
La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
Imprimir los nombres del padre, la madre y sus hijos.
También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
"""
ListaPadres = []
ListaHijos = []
Familias = int(input("Ingresa cantidad de familias: "))
for f1 in range (Familias):
    ListaPadres.append([])
    ListaHijos.append([])
    pa = input("Nombre del padre: ")
    ma = input("Nombre de la madre: ")
    ListaPadres[f1].append([pa,ma])
    Hijos = int(input("Ingresa cantidad de hijos: "))
    for f2 in range(Hijos):
        hi = input("Nombre del hijo: ")
        ListaHijos[f1].append(hi)
print("Lista de padres: ", ListaPadres)
print("Lista de hijos: ", ListaHijos)
