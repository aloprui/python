"""
Dada una lista con un número variable de cadenas, que pueden indicar por ejemplo las tareas del hogar
que hay que realizar o los platos de un menú.
 Imprime cada elemento de esta lista precedido por su número, empezando en 1. Por ejemplo:
1. Limpiar
2. Comprar Comida
3. Salir

"""

lista =["Limpiar","Comprar comida","Salir"]

for i,lista in enumerate(lista,start=1):
    print(f"{i}.{lista}")