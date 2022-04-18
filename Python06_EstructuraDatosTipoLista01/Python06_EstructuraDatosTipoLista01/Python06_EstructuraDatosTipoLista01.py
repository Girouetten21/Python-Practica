#Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
enterosLista = [1,2,3,4,5]
suma = 0
sumaW = 0
w = 0

suma = enterosLista[0] + enterosLista[1] + enterosLista[2] + enterosLista[3] + enterosLista[4]
print("Lista de numeros es: ", enterosLista)
print("Resultado de la suma lineal: ", suma)

while w < len(enterosLista):
    sumaW = sumaW + enterosLista[w]
    w = w + 1
print("Resultado de la suma en el bucle While: ", suma)