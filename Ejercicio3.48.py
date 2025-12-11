"""Definir una funció elements_parells() que donada una llista de paraules, 
només ens mostri les que estan en la posició parell. Prova-la"""

lista = """La programación es el proceso de crear instrucciones que una computadora puede entender y ejecutar. 
           Gracias a ella podemos desarrollar aplicaciones, páginas web, videojuegos y sistemas que usamos cada día. 
           Programar nos permite resolver problemas, automatizar tareas y transformar ideas en realidad usando lenguajes 
           como Python, JavaScript o C++. 
           Además, aprender a programar mejora el pensamiento lógico y la creatividad."""
lista = lista.split()

def elements_parells(lista):
    for i in range(0, len(lista), 2):
        print(lista[i], end=" ")

elements_parells(lista)
print("")