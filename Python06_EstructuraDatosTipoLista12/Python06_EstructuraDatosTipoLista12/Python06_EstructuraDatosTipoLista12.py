"""
Se desea saber la temperatura media trimestral de cuatro paises. 
Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.

a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""
ListaPaises = []
ListaTemp = []
PromedioTemp = []
Mayor = 0
for P in range(4):
    Pais = input("Ingresar el pais: ")
    ListaPaises.append(Pais)
    temp1 = int(input("Ingresar primera temperatura: "))
    temp2= int(input("Ingresar segunda temperatura: "))
    temp3 = int(input("Ingresar tercera temperatura: "))
    ListaTemp.append([temp1,temp2,temp3])
for S in range(4):
    Promedio = (ListaTemp[S][0]+ListaTemp[S][1]+ListaTemp[S][2])//3
    PromedioTemp.append(Promedio)
for M in range(1,4):
    if PromedioTemp[M] > PromedioTemp[Mayor]:
        Mayor = M
print("Lista de Paises: ", ListaPaises)
print("Lista de Temperaturas: ", ListaTemp)
print("Promedio de Temperaturas: ", PromedioTemp)
print("Pais con mayor Temperatura: ", ListaPaises[Mayor])