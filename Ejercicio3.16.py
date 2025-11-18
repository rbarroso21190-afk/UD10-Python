"""Definir una funció gran_llista() que donada una llista de número ens retorni el més gran.
Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10."""

nums = input("Introduce una lista de numeros separado por comas:")

lista = [int(x) for x in nums.split(',')]

def gran_llista(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor        
    
print("El numero mayor de la lista es:", gran_llista(lista))
         