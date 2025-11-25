"Definir una funció elimina_duplicats() que donada una llista ens retorni una nova llista sense elements duplicats."

lista = input("Introduce una lista separada por comas:")
lista = [x for x in lista.split(",")]

def elimina_duplicats(lista):
    return list(set(lista))

lista_sin_duplicados = elimina_duplicats(lista)
print(lista_sin_duplicados)