"""
Usando listas realiza las siguientes operaciones
Parte de un menú base: ["Ensalada", "Sopa", "Pasta"].
Haz una copia independiente llamada menu_hoy.
Extiende menu_hoy con los especiales: ["Pescado", "Postre"].
Retira el último plato añadido por error.
Elimina “Sopa” si está.
Escoge una posición del menú y eliminala.
Muestra el menú al revés.
Vacía por completo la lista base original y demuestra que menu_hoy no se ha visto afectada
"""

lista = ["Ensalada", "Sopa", "Pasta"]
menu_hoy = lista.copy()
menu_hoy.insert(["Pescado", "Postre"])
