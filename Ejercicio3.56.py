"""Crear una funció que donada una llista de valors numèrics, 
retorni el número d’elements on coincideix el valor i l’índex on és. 
Utilitzar enumerate. Ex: [0, 2, 3, 3, 4], retorni 3."""

lista= [0, 1, 5, 3, 4, 10, 6]

def contar_coincidencias(lista):
    contador = 0
    for index, valor in enumerate(lista):
        if index == valor:
            contador += 1
    return contador

print("Coincidencias:", contar_coincidencias(lista))

    