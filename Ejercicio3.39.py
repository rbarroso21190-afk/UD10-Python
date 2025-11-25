"""Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té qualque element duplicat o no, 
no s’ha de modificar la llista donada. Prova-la."""

lista = input("Introduce una lista de elementos separada por comas:")

lista = [x for x in lista.split(",")]


def hi_ha_duplicats(lista):
    if len(lista) != len(set(lista)):
        print("Hay un elemento duplicado")
    else:
        print("No hay ningun elemento repetido")
       
hi_ha_duplicats(lista)
