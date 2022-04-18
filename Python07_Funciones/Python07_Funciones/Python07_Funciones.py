#Desarrollar un programa con dos funciones. 
#La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
#La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
#LLamar desde el bloque del programa principal a ambas funciones.
def funcion01():
    entero = int(input("Ingresar un entero: "))
    entero = entero*entero
    print("El cuadrado del entero es: ", entero)
def funcion02():
    num1 = int(input("Ingresar primer valor: "))
    num2 = int(input("Ingresar segundo valor: "))
    producto = num1 * num2
    print("El producto de ambos numero es: ", producto)
#START
print("A continuacion se pedira un numero y se dara el cuadrado de dicho numero")
funcion01()
print("************************************************************************")
print("A continuacion se pedira dos numeros y se dara el producto de los mismos")
funcion02()