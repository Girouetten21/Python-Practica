#Plantear una función que reciba un string y retorne la cantidad de vocales
def re_vocales_cant(palabra):
    cant = 0
    for f in range (len(palabra)):
        if palabra[f] == "a" or palabra[f] == "e" or palabra[f] == "i" or palabra[f] == "o" or palabra[f] == "u":
            cant = cant + 1
    return cant
###START
palabra1 = input("Ingresar una palabra: ")
print("Cantidad de vocales: ", re_vocales_cant(palabra1))
