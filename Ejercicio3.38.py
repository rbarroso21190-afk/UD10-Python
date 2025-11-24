"""Definir una funció esta_ordenada() que donada una llista de números, ens indiqui si està ordenada en ordre ascendent, 
descendent o no està ordenada. Prova-la. Ex. esta_ordenada([3,2,1]) retorni està ordenada de forma descendent.
esta_ordenada([4,5,6]) retorni està ordenada de forma ascendent i qualsevol altres cas retorni no està ordenada."""

lista = input("Introduce una lista de numeros separados por comas:")
listaint = [int(x) for x in lista.split(",")]

def esta_ordenada(listaint):

    if listaint == sorted(listaint):
        print("La lista esta ordenada de forma ascendente")
    elif listaint == sorted(listaint, reverse=True):
        print("La lista esta ordenada de forma descendente") 
    else:
        print("La lista no esta ordenada") 

esta_ordenada([1,2,3])
esta_ordenada([3,2,1])
esta_ordenada([4,5,6])
esta_ordenada([1,3,2])