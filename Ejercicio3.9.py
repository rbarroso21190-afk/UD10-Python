"""Definir una funció sumar_llista() i una funció multiplicar_llista() que sumin i multipliqueu, respectivament, tots els valors d’una llista. 
Prova-la amb diferents exemples. Ex: sumar_llista([1,2,3,4]) retorni 10."""

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def multiplicar_lista(lista):
    multiplicacion = 1
    for numero in lista:
        multiplicacion *= numero
    return multiplicacion

entrada = input("Introduce una lista de números separados por comas:").split(",")

lista = [int(num) for num in entrada]   

print("La suma de la lista es:", sumar_lista(lista))
print("La multiplicación de la lista es:", multiplicar_lista(lista))