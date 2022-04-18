#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
def enteros(num1,num2,num3):
    promedio = 0 
    promedio = int((num1+num2+num3)/3)
    return promedio
### START
n1 = int(input("Ingresar primer numero: "))
n2 = int(input("Ingresar primer numero: "))
n3 = int(input("Ingresar primer numero: "))
print("El promedio de los tres numeros es: ", enteros(n1,n2,n3))