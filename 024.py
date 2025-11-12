import time

cadena = input("Dima una cadena de texto: ")
cadena_original= input("Dime el caracter a remplazar: ")
cadena_nueva = input("Dime el caracter nuevo: ")

if len(cadena_original) !=1 or len(cadena_nueva) !=1:
    print("Solo puedes añadir un nuevo caracter")
    time.sleep(3)
    quit()

ocurriencia ={cadena_original: cadena.count(cadena_original)}

print(f"El {cadena_original}, aparece {ocurriencia[cadena_original]} vez/veces.")

cadena_modifiacada=  cadena.replace(cadena_original, cadena_nueva)

print(cadena_modifiacada)