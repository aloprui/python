import time

cadena = input("Ingresa una cadena de texto: ")

caracter_remplazar = input("Ingresa una caracter para remplazar: ")
caracter_nuevo = input("Ingresa una caracter para nuevo: ")

if len(caracter_remplazar) != 1 or len(caracter_nuevo) != 1:
    print("Solo puedes introducir un caracter para remplazar")
    time.sleep(3)
    exit(1)

cadena =cadena.replace(caracter_remplazar, caracter_nuevo)
print(f"El texto es: {cadena}")