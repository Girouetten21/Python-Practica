"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
"""
def cargar_listas():
    l1 = []
    l2 = []
    for f in range (5):
        v1 = input("Ingresar nombre del articulo: ")
        v2 = int(input("Ingresar precio del articulo: "))
        l1.append(v1)
        l2.append(v2)
    return(l1,l2)

def imprimir_listas(articulos,precios):
    print("Lista de articulos: ", articulos)
    print("Lista de precios: ", precios)

def articulo_mayor(articulos,precios):
    mayor = 0
    for f in range (1,len(precios)):
        if precios[f] > precios[mayor]:
            mayor = f
    print("El articulo mayor es: ", articulos[mayor], "-", "Con un precio de: ", precios[mayor])

def presupuesto(articulos,precios):
    v1 = int(input("Ingresar presupuesto: "))
    for f in range (len(precios)):
        if precios[f]<=v1:
            print("Articulo: ", articulos[f], "-", "Precio: ",precios[f])

###START
print("*********************************")
lista1,lista2 = cargar_listas()
print("*********************************")
imprimir_listas(lista1,lista2)
print("*********************************")
articulo_mayor(lista1,lista2)
print("*********************************")
presupuesto(lista1,lista2)
print("*********************************")