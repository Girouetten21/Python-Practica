"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. 
"""

valor = float(input("Ingresa un numero REAL: "))
for i in range(1,11):
    valor2 = float(input("Ingresar valor real a sumar: "))
    valor = valor2 + valor
print("La suma de los 10 digitos es: ", valor)