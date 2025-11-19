"""Definir una funció comptar_vocals() que donada una paraula, compti el número de vegades que apareix cada vocal. 
Ex: comptar_vocals(“Ratapinyada”) retorni1 HI ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s."""

palabra = input("Introduce una palabra:")
palabra = palabra.lower()

def contar_vocals(palabra):
    vocales = "aeiou"
    contadorvoc = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letra in palabra:
        if letra in vocales:
            contadorvoc[letra] += 1
                

            
    print("La palabra es: {}".format(palabra))
    print("Hay un total de: \n{}:a\n{}:e\n{}:i\n{}:o\n{}:u".format(contadorvoc["a"],contadorvoc["e"],contadorvoc["i"],contadorvoc["o"],contadorvoc["u"]))

    return contadorvoc

contar_vocals(palabra)