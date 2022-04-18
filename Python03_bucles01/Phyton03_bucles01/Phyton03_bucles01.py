"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1. 
Dejar como comentario dentro del código fuente el enunciado del problema.
"""

suma = 0
valor=int(input("Ingresar valor: "))
while valor!=-1:
    suma=suma+valor
    valor=int(input("Ingresar valor a sumar: "))
print("La suma de los valores ingresados es: ", suma)
