#Definir una función que cargue una lista con palabras y la retorne.
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
def cargar_lista():
    l = []
    v = int(input("Cantidad de palabras. "))
    for f in range(v):
        palabra = input("Ingresar palabra a la lista: ")
        l.append(palabra)
    return l

def mas_de_5_char(lista):
    print("Lista completa: ", lista)
    for palabra in lista:
        if len(palabra) >= 5:
            print("Palabra con mas de 5 caracteres: ", palabra)
      
###START
li = cargar_lista()
mas_de_5_char(li)