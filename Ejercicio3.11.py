"""Definir una funció es_palindrom() que retorni vertader si li passem un palíndrom i fals en cas contrari. 
Un palíndrom és una paraula que s’escriu igual d’esquerra a dreta i de dreta a esquerra. Per exemple: radar, ara, civic, rallar, tapat, simis, refer, …"""

def es_palindrom(cadena):
    cadena_invertida = cadena[::-1]
    if cadena == cadena_invertida:
        return True
    else:
        return False
    

palofra = input("Introduce una palabra:")

if es_palindrom(palofra) == True:
    print("La palabra es un palíndrom") 
else:
    print("La palabra no es un palíndrom")