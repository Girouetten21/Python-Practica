"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""
valor = 0
listaDia = []
listaNoche = []
print("A continuacion ingresar los sueldos de los empleados del turno de la mañana")
for f in range (4):
    valor = input("Ingresa el sueldo: ")
    listaDia.append(valor)
print("A continuacion ingresar los sueldos de los empleados del turno de la tarde")
for f in range (4):
    valor = input("Ingresa el sueldo: ")
    listaNoche.append(valor)
print("Lista del suedo de los empleados del turno de la mañana: ", listaDia)
print("Lista del suedo de los empleados del turno de la tarde: ", listaNoche)
