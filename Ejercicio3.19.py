"""Definir una funció que donada una cadena, avaluï quantes lletres majúscules hi ha.
Prova-la amb diferents exemples."""

cadena = input("Introduce una cadena de texto:")

def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

print("El número de letras mayúsculas en la cadena es:", contar_mayusculas(cadena))