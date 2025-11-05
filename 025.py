paises = ["España", "Argentina","Perú"]
sel = 1
cont = 0

while sel != 5:
    print("1. Imprimir alfabéticamente en orden ascendente")
    print("2. Imprimir alfabéticamente en orden descendente")
    print("3. Añadir País")
    print("4. Eliminar País")
    print("5. Salir")

    cont += 1
    sel = int(input("Elija una opción (1-5): "))

    if sel < 1 or sel > 5:
        print("Debe elegir un número entre 1 y 5.")
        print("Intento número:", cont)
        continue

    match sel:
        case 1:
            print("Lista de paises asccendente")
            paises.sort()
            print(paises)
            print("\n")

        case 2:
            print("Lista de paises descendente")
            paises.sort(reverse=True)
            print(paises)
            print("\n")

        case 3:
            if len(paises) > 6:
                print("No se puede añadir más de 6 paies.")
            else:
                nuevo = input("Dime el nuevo Pais: ").strip()
                if nuevo == "":
                    print("No se puede añadir uno vacío")
                elif nuevo in paises:
                    print("Este pais ya se encuentra en la lista")
                else:
                    paises.append(nuevo)
                    print("Añadido correctamente")
                    print("Lista nueva: ", paises)
                    print("\n")

        case 4:
            borrar = input("Dime el pais que quieres borrar: ")
            if borrar in paises:
                paises.remove(borrar)
                print("Pais borrado.")
                print("Lista nueva: ", paises)
                print("\n")
            else:
                print("Pais no encontrado")

        case 5:
            print("Gracias por usar el programa.")
            print("Número total de intentos:", cont)
            break

        case _:
            print("Debe elegir un número entre 1 y 5.")

    if sel!= 5:
        print("Terminado correctamente")