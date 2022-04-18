#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. 
#Contar cuántas personas son más altas que el promedio y cuántas más bajas.
valor = 0.0
lista = []
listaSuma = 0.0
promedio = 0.0
estaturaAlta = 0
estaturaBaja = 0
for f in range (5):
    valor = float(input("Ingresar altura: "))
    lista.append(valor)
    listaSuma = listaSuma + valor

promedio = listaSuma / 5

for f in range (5):
    if lista[f] > promedio:
        estaturaAlta = estaturaAlta + 1
    else:
        estaturaBaja = estaturaBaja + 1

print("Lista: ", lista)
print("Promedio: ", promedio)
print("Personas Altas: ", estaturaAlta, "-", "Personas Bajas", estaturaBaja)