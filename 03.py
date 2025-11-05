"""Usando listas realiza las siguientes operaciones.:
Parte A: Parte de una lista vacía de asistentes. Pide nombres por consola y añadelos a la lista hasta que el usuario escriba “fin”.
Parte B: Muestra cuántas veces aparece un nombre que te indique el usuario.
Parte C: muestra por consola la primera posición en la que aparece el nombre anterior y elimina esta ocurrencia.
Parte D: Inserta al inicio (posición 0) un asistente VIP..
Muestra la lista final.
Ejemplo:
Entrada: Juan, Ana, Ana, Luis, fin; consulta “Ana”; VIP “Directora”.
Salida: count("Ana")=2, index("Ana")=1; tras remove("Ana"): […]; tras insert(0,"Directora"): ["Directora", …]
"""
#A
asistentes = []

while True:
    nombre = input("Dime el nombre: ")
    if nombre.strip().lower() == "fin":
        break
    asistentes.append(nombre)
print(f"Asistentes: {asistentes}")

#B
aparece = input("Dime el nombre, para saber las repeticiones: ")
print(f"El nombre aparece: {asistentes.count(aparece)}, vez/veces")

#C
numero = asistentes.index(aparece)
print(f"El nombre aparece por primera vez en: {numero+1}")
asistentes.pop(numero)

#D
nombre3 = input("VIP: ")
asistentes.insert(0, nombre3)

print(f"Asistentes: {asistentes}")