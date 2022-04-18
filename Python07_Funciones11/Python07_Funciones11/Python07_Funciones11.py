"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $100.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""
def carga_lista():
    li = []
    for f in range (10):
        valor = int(input("Ingresar sueldo: "))
        li.append(valor)
    return (li)

def print_sueldos(lista):
    print("Lista: ", lista)

def mayormenor_sueldos(lista):
    mayor = 0
    menor = 0
    for f in range (len(lista)):
        if lista[f] >= 100:
            mayor = mayor + 1
        else:
            menor = menor + 1
    print("Cantidad de sueldos mayores: ", mayor)
    print("Cantidad de sueldos menores: ", menor)

def promedio_sueldos(lista):
    promedio = 0
    for f in range (len(lista)):
        promedio = promedio + lista[f]
    promedio = promedio / len(lista)
    print("Promedio del sueldo es: ", promedio)

###START
print("*****************************")
lista1 = carga_lista()
print("*****************************")
print_sueldos(lista1)
print("*****************************")
mayormenor_sueldos(lista1)
print("*****************************")
promedio_sueldos(lista1)