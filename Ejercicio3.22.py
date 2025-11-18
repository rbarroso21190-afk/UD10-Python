"""Definir una funció mostrar_majors_que() que donada una tupla de números enters, imprimeixi tots els superiors a un altre número donat. 
Per provar que funciona bé, escriure un programa que permeti introduir els valors enters de la tupla  i ens digui tots els que són majors de 18 anys."""

tupla = input("Introduce una serie de números enteros separados por comas:")

def mostrar_majors_que(tupla):
    menores = 0
    mayores = 0
    tupla = [int(x) for x in tupla.split(",")]
    for x in tupla:
        if x > 18:
            mayores += 1
        else:
            menores += 1

    print("Números mayores de 18: {}".format(mayores))
    print("Números menores o iguales a 18: {}".format(menores))
  
mostrar_majors_que(tupla)