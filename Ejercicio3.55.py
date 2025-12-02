"""Crear una funció que donada una llista, retorni un diccionari que tingui com a clau: 
els valors de la llista i com a valor el seu índex dins la llista. Utilitzar enumerate. 
Ex: (‘casa’,’cotxe’,’cadira’,’taula’) retorni {‘casa’:0, ‘cotxe’:1, ‘cadira’:2, ‘taula’:3}."""

lista = ["montaña", "rio", "estrella", "camino", "lluvia"]

def funcion(lista):
    diccionario = {valor: indice for indice, valor in enumerate(lista)}
    return diccionario

posicion = funcion(lista)
print(posicion)