nombre1 = str(input("Ingresar nombre 1: "))
altura1 = float(input("Ingresar su altura (Ej. 1.75): "))
nombre2 = str(input("Ingresar nombre 2: "))
altura2 = float(input("Ingresar su altura (Ej. 1.75): "))

if altura1>altura2:
    print("El usuario", nombre1, "tiene una altura mayor: ", altura1)
else:
    print("El usuario", nombre2, "tiene una altura mayor: ", altura2)