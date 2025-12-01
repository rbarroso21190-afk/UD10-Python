"""Crear una funció que donades dues llistes, les concateni amb un connector. Utilitzar zip. 
Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’]."""

lista1 = ["casa", "libro", "gato", "sol", "árbol"]
lista2 = ["mar", "nube", "fuego", "piedra", "cielo"]
conector = "-"

def concatenar(lista1, lista2, conector):
    return [a + conector + b for a, b in zip(lista1, lista2)]


resultado = concatenar(lista1, lista2, conector)
print(resultado)