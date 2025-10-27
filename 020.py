"""
Crea una calculadora que haga las operaciones de sumar multiplicar dividir
 y restar de dos números enteros introducidos por teclado.

El resultado se dará en dos decimales.

Debe ofrecerse el menú mientras el usuario no escriba “salir”.
Dará igual que sea mayúsculas o minúsculas o que tenga espacios por delante y por detrás.

Controlar que son números enteros los que se mete.

Controlar que la división por cero es un error.
"""

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opciones = input("Elige una opción: ").strip().lower()

    if opciones == "5":
        print("Saliendo...")
        break
    try:
        numero1= int(input("Dime el primer numero: "))
        numero2= int(input("Dime el segundo numero: "))


        match opciones:
            case "1":
                resultado1 = numero1 + numero2
                print(resultado1)
            case "2":
                resultado2 = numero1 - numero2
                print(resultado2)
            case "3":
                resultado3 = numero1 * numero2
                print(resultado3)
            case "4":
                if numero2 == 0:
                    print("Error: No se puede dividir entre cero")
                else:
                    print("Resultado:", round(numero1 / numero2, 2))
            case _:
                print("No se puede")
    except ValueError:
        print("Error")