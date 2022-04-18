#Crear dos listas paralelas. 
#En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
#Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
#Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
listaNombres = []
listaSueldos = []
pos = 0
cantidadEmpleados = int(input("Ingresar cantidad de empleados: "))
for f in range (cantidadEmpleados):
    Nombre = input("Ingresar nombre del empleado: ")
    Sueldo = int(input("Ingresar sueldo del empleado: "))
    listaNombres.append(Nombre)
    listaSueldos.append(Sueldo)
print("Empleados: ", listaNombres)
print("Sueldos: ", listaSueldos)
while pos < len(listaSueldos):
    if listaSueldos[pos] > 10000:
        listaSueldos.pop(pos)
        listaNombres.pop(pos)
    else:
        pos = pos + 1
print("Nueva Empleados: ", listaNombres)
print("Nueva Sueldos: ", listaSueldos)