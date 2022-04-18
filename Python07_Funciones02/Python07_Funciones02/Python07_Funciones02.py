#Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
#Llamarla desde el bloque principal del programa 3 veces con string distintos.
def cant_vocales(palabra):
    cant = 0
    for f in range (len(palabra)):
        if palabra[f] == "a" or palabra[f] == "e" or palabra[f] == "i" or palabra[f] == "o" or palabra[f] == "u":
            cant = cant + 1
    print("La cantidad de vocales es: ", cant)
### START
palabra01 = input("Ingresar palabra: ")
cant_vocales(palabra01)
palabra02 = input("Ingresar palabra: ")
cant_vocales(palabra02)