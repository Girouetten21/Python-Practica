"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.
"""

Clave = input("Ingresar contraseña: ")

if len(Clave) < 10 and len(Clave) > 20:
    print("ERROR: La clave no contiene 10-20 caracteres")
else:
    print("La clave contiene 10-20 caracteres")
