inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}

inventario = inventario_inicial.copy()

avisos =[]
for cod in ventas:
    if cod not in inventario:
        inventario[cod]= 0
        avisos.append("Ha sido añadido correctamente.")
    else:
        inventario[cod] -=1

if avisos:
    print("\n".join(avisos))
    print(inventario)

for cod, cantidad in reposiciones.items():
    inventario.setdefault(cod, 0)
    inventario[cod] += cantidad

print(inventario)

num_referencias = len(inventario)
unidades_totales = sum(reposiciones.values())

print("Informe: ")
print(f"Numero de referencia: {num_referencias}")
print(f"Unidades totales: {unidades_totales}")

inventario_filtrado={cod: stock for cod, stock in inventario.items() if stock> 0}
print(inventario_filtrado)

codigo = input("\nIntroduce un código de producto: ").strip().upper()
print(inventario.get(codigo, "No existe"))

del inventario