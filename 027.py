usuarios = {"Marta", "David", "Elvira", "Juan" , "Marcos"}
administradores = {"Juan","Marta"}

administradores.discard("Juan")

administradores.add("Marcos")

print(usuarios)
print(administradores)

for usuario in usuarios:
    if(usuario in administradores):
        print("Es admistrador.")
    else:
        print("No es admistrador.")