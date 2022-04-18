#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
def mascaracteres(maschar):
    pos = 0
    for f in range (1,len(maschar)):
        if len(maschar[pos]) < len(maschar[f]):
            pos = f
    return maschar[pos]
###START
palabras1=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras1))