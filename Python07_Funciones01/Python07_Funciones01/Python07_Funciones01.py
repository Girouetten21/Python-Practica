#Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
#Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
def numero_menor():
    lista = []
    for f in range (3):
        numero = int(input("Ingresar numero a la lista: "))
        lista.append(numero)
        menor = 0
    for f2 in range (1,3):
        if lista[f2] < lista[menor]:
            menor = f2
    print("El numero menor es: ", lista[menor])
### DEBUG
numero_menor()
numero_menor()