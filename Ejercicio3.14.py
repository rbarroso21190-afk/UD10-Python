"""Definir una funció crear_punts() que agafi una llista de números i que pinti per pantalla tants punts com el valor de cada número de la llista. 
Entre els elements de la llista, hi ha d’haver un salt de línia. Ex: crear_punts([2,3,4]) mostri per pantalla el següent:
..
...
.... """

nums = input("Introduce numeros enteros separados por comas:")

lista_numeros = [int(x) for x in nums.split(',')]

def crear_punts(lista_numeros):
    for numero in lista_numeros:
        print('.' * numero)

crear_punts(lista_numeros)