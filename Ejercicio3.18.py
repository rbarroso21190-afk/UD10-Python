"""Definir una funció filtrar_paraules() que donada una llista de paraules i un número x, 
retorni totes les paraules que tingui més d’x-caràcters."""

l_palabras = input("introduce una lista de palabras separadas por comas:")
x = int(input("introduce un numero entero para un minimo de letras:"))

def filtrar_paraules(l_palabras, x):
    l_resultado = []
    for palabra in l_palabras.split(","):
        if len(palabra) > x:
            l_resultado.append(palabra)
    return l_resultado

print("La lista de palabras es:", filtrar_paraules(l_palabras, x))