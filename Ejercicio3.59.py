"""Crear una llista dels 10 primers números elevats a una potència donada. 
Utilitzar list comprehensions. 
Ex: Si volem el quadrat dels números de la llista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 
retorni [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 
si la volem del cub retorni [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] i així successivament."""

potencia = int(input("Introduce el numero para calcular su potencia:"))
lista = [x ** potencia for x in range(0,10)]
print(lista)