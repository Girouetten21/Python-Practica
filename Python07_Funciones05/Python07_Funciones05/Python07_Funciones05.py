#Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
def re_perimetro(l1):
    perimetro = 4*l1
    return perimetro
### START
lado1 = int(input("Ingresar primer lado del cuadrado: "))
print("El perimetro del cuadrado es: ", re_perimetro(lado1))