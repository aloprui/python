""" Cosas a cambiar de el 025 """
# Antes
paises = ["España", "Argentina", "Perú"]
nuevo = input("Introduce un país: ").capitalize()
if nuevo not in paises and len(paises) < 6:
    paises.append(nuevo)

# Después
paises = {"España", "Argentina", "Perú"}
nuevo = input("Introduce un país: ").capitalize()
if len(paises) < 6:
    paises.add(nuevo)

# Antes
borrar = input("Introduce país a eliminar: ").capitalize()
if borrar in paises:
    paises.remove(borrar)
# Después
borrar = input("Introduce país a eliminar: ").capitalize()
if borrar in paises:
    paises.discard(borrar)

#Mostrar ordenados:
print(sorted(paises))               # ascendente
print(sorted(paises, reverse=True)) # descendente