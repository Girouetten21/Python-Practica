"""
Realizar la carga de enteros por teclado. 
Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.
"""

condicionStr = "Si"
valor = int(input("Ingresar numero: "))
while condicionStr == "Si":
    valor2 = int(input("Ingresar numero a sumar: "))
    valor = valor + valor2
    condicionStr = input("¿Si desea continuar sumando? Si/No:" )
print("El resultado de los numeros sumados es: ", valor)
