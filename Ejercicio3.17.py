"""Definir una funció paraula_mes_llarga() que donada una llista de paraules, 
retorni la que té més caràcters. Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula."""

l_palabras = input("Introduce una lista de palabras separadas por comas:")

def palabra_mas_larga(lista):
    lista_palabras = lista.split(",")
    palabra_mas_larga = ""
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

print("La palabra más larga es:", palabra_mas_larga(l_palabras))