#Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.   

nombre1 = str(input("Ingresar primer nombre: "))
nombre2 = str(input("Ingresar segundo nombre: "))
if nombre1>nombre2:
    print("El nombre mayor alfabeticamente es: ", nombre1)
else:
    print("El nombre mayor alfabeticamente es: ", nombre2)