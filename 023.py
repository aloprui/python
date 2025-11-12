import time

cadena = input("Dime una cadena de texto: ")

caracter_unicos = set(cadena)
print(f"Los caracteres unicos son: {caracter_unicos}")

sustituir = input("Dime el caracter a remplazar: ")
nuevo = input("Dime una nueva cadena: ")

if len(sustituir) != 1 or len(nuevo) != 1:
    print("Error.")
    time.sleep(3)
    exit()

resultado = cadena.replace(sustituir, nuevo)
print(f"El resultado es: {resultado}")