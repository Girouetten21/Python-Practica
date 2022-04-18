#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
#Mostrar el nombre de persona menor en orden alfabético.
valor = ""
lista=[]
for f in range (5):
    valor = input("Ingresar nombre: ")
    lista.append(valor)
nombreMenor = lista[0]
for f in range (1,5):
    if lista[f] < nombreMenor:
        nombreMenor = lista[f]
print("Lista de nombres: ", lista)
print("Persona con el nombre menor alfabeticamente: ", nombreMenor)