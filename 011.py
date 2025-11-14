listas = [[1,2,3],[4,5], [6,7,8,9],[10]]

unir = [x for sublista in listas for x in sublista]
print(unir)


par = [x for sublista in listas for x in sublista if x %2 == 0]
print(par)


matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(traspuesta)