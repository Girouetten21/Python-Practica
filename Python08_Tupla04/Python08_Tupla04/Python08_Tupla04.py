"""
Almacenar los nombres de 5 productos y sus precios.
Utilizar una lista y cada elemento una tupla con el nombre y el precio.

Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def cargar():
    l = []
    for f in range(5):
        v1 = input("Ingresar nombre del producto: ")
        v2 = int(input("Ingresar valor del producto: "))
        l.append((v1,v2))
    return l

def mostrar_lista(lista):
    print("Lista completa: ", lista)

def producto_entre_10_15(lista):
    for nombre_pro,precio_pro in lista:
        if precio_pro >= 10 and precio_pro <= 15:
            print("Producto: ", precio_pro)
###START
li = cargar()
mostrar_lista(li)
producto_entre_10_15(li)
