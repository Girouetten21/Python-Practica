#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
def enteros(num1,num2,num3):
    lista = [num1,num2,num3]
    mayor = 0
    for M in range(1,3):
        if lista[M] > lista[mayor]:
            mayor = M
    print("Numero mayor es: ", lista[mayor])
def cargar_numeros():
    valor1 = int(input("Ingresar primer valor: "))
    valor2 = int(input("Ingresar segundo valor: "))
    valor3 = int(input("Ingresar tercer valor: "))
    enteros(valor1,valor2,valor3)
### START
cargar_numeros()