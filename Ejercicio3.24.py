"Variar l’exercici anterior, perquè enlloc de la lletra a, sigui una lletra introduïda per teclat per l’usuari."

comienzo_letra = str(input("Introduce la letra por la que deben comenzar los nombres:"))
lista_prov = input("Introduce una llista de noms separats per comes:")

lista_nombres = lista_prov.split(",")

def nums_que_comencen_per(lista_nombres, comienzo_letra):
    contador = 0
    comienzo_letra = comienzo_letra.lower()
    letra = comienzo_letra[0]  
    
    for nombre in lista_nombres:
        nombre_limpio = nombre.strip().lower()
        if nombre_limpio.startswith(letra):
            contador += 1

    print("El número de palabras que comienzan por la letra '{}' es: {}".format(letra, contador))

nums_que_comencen_per(lista_nombres, comienzo_letra)