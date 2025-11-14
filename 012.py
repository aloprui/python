lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8]

pares = [(x,y) for x in lista1 for y in lista2 if (x+y) %2 == 0]
print(pares)