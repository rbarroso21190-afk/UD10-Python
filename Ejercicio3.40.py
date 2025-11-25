"""Definir una funció llista_20_elements() que retorni una llista de 20 elements creats aleatòriament entre 1 i 100. 
Provar amb la funció anterior si s’han generat elements duplicats o no."""

import random

def llista_20_elements():
    lista = [random.randint(1, 100) for _ in range(20)]
    return lista

def hi_ha_duplicats(lista):
    if len(lista) != len(set(lista)):
        print("Hay un elemento duplicado")
    else:
        print("No hay ningun elemento repetido")

lista = llista_20_elements()
print("La lista es:{}".format(lista))

hi_ha_duplicats(lista)
