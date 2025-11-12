taller = {"Daniel","Antonio Manuel","Hugo","Ale"}

print("Dime nombres para insertar(fin para terminar)")
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre == "fin":
        print("Terminando")
        break
    elif not nombre:
        print("Error, no se puede bacío.")
        break
    else:
        taller.add(nombre)
        print(taller)

lotes = input("Introduce un nombre separados por comas").strip()
nuevos ={n.strip() for n in lotes.split(",") if n.strip != ("")}
taller.update(nuevos)
print(taller)

taller_copia = taller.copy()

baja = input("Dime el nombre que desea darse de baja").strip()
if baja in taller:
    taller.remove(baja)
    print(taller)
else:
    print("Error, no se encontro")

consulta = input("Introduce un nombre, para ver si esta inscrito").strip()
if consulta in taller:
    print(f"{consulta}Se encuentra en el taller.")
else:
    print(f"{consulta}No se encontro en el taller.")

grupo = {"Juan","Maria","Daniel"}
print("¿Esta alguien de este grupo?")
if taller.intersection(grupo):
    print("Hay almenos una persona que se encuentra.")
else:
    print("No se encuentra ninguna persona.")

print(f"Numeros de inscritos: {len(taller)}")
print("Lista ordenada alfabeticamente: ")
for nombre in sorted(taller):
    print("-", nombre)