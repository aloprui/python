"""Realiza un programa que muestre por consola si un número entero es impar:

Se ejecutará indefinidamente hasta que el usuario introduzca un número entero impar.

Controlará la excepción ValueError que se puede producir en este caso al convertir a entero algo que no es un entero.
En este caso también indicará que debe introducir un número impar y volverá a pedirlo.
"""

while True:
    try:
        numero = int(input("Dime un numero: "))

        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
            break
    except ValueError:
        print("Tienes que introducir un numero impar")