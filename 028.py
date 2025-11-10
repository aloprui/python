print("Pizzería La Beata")
dinero = input("Ingrese el dinero: ").strip()
print(f"Con ese precio: {dinero} , tenemos.")

barbacoa = 10.50
peperoni = 9.50
cuatroQuesos = 12.50
marganita = 8.50

print("Pizas disponibles:")
print(f"1. Pizza Barbacoa - {barbacoa}")
print(f"2. Pizza Peperoni - {peperoni}")
print(f"3. Pizza Cuatro Quesos - {cuatroQuesos}")
print(f"4. Pizza Marganita - {marganita}")

opcion = int(input("Dime la Pizza que quieras(1-4): "))

if opcion == 1:
    pizza = "Barbacoa"
    precio = barbacoa
elif opcion == 2:
    pizza = "Peperoni"
    precio = peperoni
elif opcion == 3:
    pizza = "Cuatro Quesos"
    precio = cuatroQuesos
elif opcion == 4:
    pizza = "Marganita"
    precio = marganita
else:
    print("Pizza no encontrada.")
    exit()

print(f"Has elegido la Pizza: {pizza} - {precio}")

queso = 1.50
champiñones = 1.00
jamon = 2.50

print("¿Se te apetece algun ingrediente extra?")
print(f"1. Queso - {queso}")
print(f"2. Champiñones - {champiñones}")
print(f"3. Jamón - {jamon}")
print(f"4. No añadir extras.")

total_extras = 0
extras_elegido = []

while True:
    extra = int(input("Ingrese la extra que quieras(1-4): "))
    if extra == 1:
        total_extras += queso
        extras_elegido.append(queso)
    elif extra == 2:
        total_extras +=champiñones
        extras_elegido.append(champiñones)
    elif extra == 3:
        total_extras += jamon
        extras_elegido.append(jamon)
    elif extra == 4:
        break
    else:
        print("Opcion no valida.")

total_pedido = precio + total_extras
total_pedido = round(total_pedido, 2)
print(f"El total del pedido es: {total_pedido}")

if dinero >= total_pedido:
    cambio = round(dinero - total_pedido,2)

    print("\n--- SU PEDIDO ---")
    print(f"- {pizza} ${precio}")
    for nombre, precio in extras_elegido:
        print(f"- {nombre} ${precio}")
    print(f"\nTotal del pedido: ${total_pedido}")
    print(f"Su cambio de ${dinero} es: ${cambio}")
    print("\nGracias por su visita")

else:
    print("\nNo tienes suficiente dinero para pagar el pedido.")
    print("Por favor, vuelve a empezar.")