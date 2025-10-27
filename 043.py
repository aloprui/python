"""
Script que cuente las ocurrencias de cada carácter de una cadena de texto, que puede ser introducida desde el teclado.
No uses set ni dict
No cuentes espacios en blanco.
No se diferencia entre caracteres en mayúsculas y en minúsculas.
"""

frase = "Betis: "
frase = frase.lower()

frase = frase.replace(" ", "")

contados = []

for caracter in frase:
    if caracter is not frase:
        contador = 0
        for c in frase:
            if c == caracter:
                contador += 1
        print(f"'{caracter}' aparece {contador} vez/veces.")
        contados.append(caracter)