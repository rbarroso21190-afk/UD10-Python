"""Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem. Utilitzar map. 
Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase."""

def lenp(frase):
    palabras = frase.split()                 
    longitudes = list(map(len, palabras))   
    return longitudes

frase = input("Introduce una frase:")
resultado = lenp(frase)
print("La longitud de la palabra es {}".format(resultado))