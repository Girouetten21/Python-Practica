#Definir una lista que almacene por asignación los nombres de 5 personas. 
#Contar cuantos de esos nombres tienen 5 o más caracteres.
lista = ["","","","",""]
contar = 0
for f in range(len(lista)):
    lista[f] = str(input("Ingresar nombre de personal: "))
    if len(lista[f]) >= 5:
        contar = contar + 1
print("Nombres con 5 caracteres o mas son: ", contar)