import copy

calificacciones = [
    {'alumno': 'Ana','modulo': 'Programacion' , 'nota': 7.5},
    {'alumno': 'Luis','modulo': 'Sistemas' , 'nota': 6.0},
    {'alumno': 'Ana','modulo': 'Sistemas' , 'nota': 8.0},
    {'alumno': 'Marta','modulo': 'Programacion' , 'nota': 9.0},
    {'alumno': 'Marta','modulo': 'Programacion' , 'nota': 10.0}
]

alumnos ={}
for calificacion in calificacciones:
    alumno =calificacion['alumno']
    nota =calificacion['nota']
    modulo = calificacion['modulo']
    alumnos.setdefault(alumno,{}).setdefault(modulo,[]).append(nota)

print(alumnos)

medias ={}

for alumno, modulos in alumnos.items():
    notas_max =[max(nota) for nota in modulos.values()]
    medias[alumno] = sum(notas_max)/len(notas_max)

print(medias)

modulos = {}
for alumno, modulos_alumno in alumnos.items():
    for modulo, notas in modulos_alumno.items():
        modulos.setdefault(modulo,{})[alumno]=max(notas)
print(modulos)

aprobados = {alumno:nota for alumno, nota in medias.items() if nota >= 5}
print(aprobados)

correcciones = {'Ana': {'Programación': +0.75}}
alumnos_corregidos = copy.deepcopy(alumnos)

for alumno, modulos_corr in correcciones.items():
    for modulo, cambio in modulos_corr.items():
        notas = alumnos_corregidos.get(alumno, {}).get(modulo)
        if notas:
            notas[-1] += cambio
print(alumnos_corregidos)


def eliminar_nota(alumnos, alumno, modulo, indice):
    nota_eliminada = alumnos[alumno][modulo].pop(indice)
    print(f"Nota {nota_eliminada} eliminada de {alumno} en {modulo}.")

    if not alumnos[alumno][modulo]:
        del alumnos[alumno][modulo]
        print(f"Se ha eliminado el módulo {modulo} de {alumno}.")

    if not alumnos[alumno]:
        del alumnos[alumno]
        print(f"Se ha eliminado completamente al alumno {alumno}.")

    return nota_eliminada