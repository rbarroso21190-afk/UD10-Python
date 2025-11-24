"""Definir una funció eliminarcapicua() que donada una llista, elimini el primer i el darrer element 
de la llista i ens retorni una nova llista sense aquest dos elements. Prova-la"""

def eliminacapicua():
    lista = input("Introduce una lista de elementos separados por comas:")
    lista = lista.split(",")
    rmlista = lista[1:-1]
    print(rmlista)
    
eliminacapicua()