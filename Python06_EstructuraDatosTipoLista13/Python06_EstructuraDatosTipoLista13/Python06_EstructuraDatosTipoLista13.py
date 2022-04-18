"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el empleado que falto menos días.
"""
lista = []
listaFaltas = []
listaInasistencias = []
posicionInasis = 0
for f in range (3):
    Empleado = input("Ingresar nombre de empleado: " )
    lista.append(Empleado)
    Faltas = int(input("¿Cuantos dias falto al mes?: "))
    listaFaltas.append([])
    listaInasistencias.append([])
    listaInasistencias[f].append(Faltas)
    for f2 in range(Faltas):
        DiasFaltas = int(input("Ingresar dias que falto: "))
        listaFaltas[f].append(DiasFaltas)
for f3 in range (len(lista)):
    print("Empleado: ",lista[f3],"Falto los dias: ", listaFaltas[f3])
    print("Inasistio un total de: ", listaInasistencias[f3], "dias")
for f4 in range(1,3):
    if listaInasistencias[f4] < listaInasistencias[posicionInasis]:
        posicionInasis = f4
print("El empleado con menos falta es: ", lista[posicionInasis])