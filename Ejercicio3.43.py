"""Definir una funció index_paraula() on donada una llista ordenada de paraules, 
ens retorni l’índex on es troba una paraula determinada o -1 en cas que no hi sigui."""

lista = input("Introduce una lista de palabras separada por espacios:")
lista = lista.split()

def index_paraula(lista):
    palabra = input("Introduce la palabra que quieres buscar:")

    if palabra in lista:
        indice = lista.index(palabra)
        print("{} está en la posición {}".format(palabra, indice))
        return indice
    else:
        print("-1")
        return -1

index_paraula(lista)