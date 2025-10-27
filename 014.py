"""
Programa que pida 3 números y muestre la media ponderada entre ellos, 15% la primera 35% la segunda y 50% la tercera.
Se debe controlar la excepción ValueError para saber si es un float lo que han introducido o no.
Se mostrará la media ponderada con dos decimales. (:.2f)
"""

while True:
    try:
        numero1 = float(input("Dime el primer numero: "))
        numero2 = float(input("Dime el segundo numero: "))
        numero3 = float(input("Dime el tercer numero: "))

        media = (numero1 * 0.15) + (numero2 * 0.35) + (numero3 * 0.50)

        print(f"La media es:  {media:.2f}" )
        break

    except ValueError:
        print("Numero no válido")