"""Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent. 
Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. 
Ex: def Passar_a_Numero(llista): -- retorni el número que corresponen els dígits."""

from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)

entrada = input("Introduce una lista de digitos separado por comas:")
entrada = entrada.replace(",", " ")
lista = [int(x) for x in entrada.split()]

resultado = Passar_a_Numero(lista)
print("El numero resultante es:", resultado)
