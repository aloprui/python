lista = [15, 23.5, 60, 11.99]

for i in range(len(lista)):
    precio_antes = lista[i]

    if precio_antes < 0:
        continue

    if i % 2 == 0:
        lista[i] = precio_antes * 0.9
    else:
        lista[i] = precio_antes * 0.8

    print(f"indice_lista={i}, precio_antes={precio_antes:.2f}, precio_después={lista[i]:.2f}")

