palabras = ["python","java","javascript","go","rust","",""]

diccionario = {p.strip(): len(p.strip()) for p in palabras}
print(diccionario)

diccionario2= {p.strip(): len(p.strip()) for p in palabras if p.strip() != ""}
print(diccionario2)


diccionario3 = {
    (p.strip().upper() if len(p.strip()) > 5 else p.strip().lower()): len(p.strip())
    for p in palabras
    if p.strip() != ""
}

print(diccionario3)