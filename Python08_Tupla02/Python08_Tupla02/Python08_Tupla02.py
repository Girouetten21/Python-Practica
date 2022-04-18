"""
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados 
y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga 
y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.
"""
def cargar_datos():
    li = []
    nom = input("Ingresar nombre del empleado: ")
    suel = int(input("Ingresar sueldo del empleado: "))
    li.append(nom)
    li.append(suel)
    empleadoTupla = tuple(li)
    return empleadoTupla

def empleado_mayor(tu1,tu2):
    if tu1[1] > tu2[1]:
        print("El empleado con mejor sueldo es: ", tu1[0], ", sueldo: ", tu1[1])
    else:
        print("El empleado con mejor sueldo es: ", tu2[0], ", sueldo: ", tu2[1])
###START
empleado1 = cargar_datos()
empleado2 = cargar_datos()
empleado_mayor(empleado1, empleado2)
