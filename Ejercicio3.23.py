"Definir una funció nums_que_comencen_per() que donat una llista de noms, ens digui quants comencen per la lletra a."

lista_prov = input("Introduce una llista de noms separats per comes:")

lista_nombres = lista_prov.split(",")

def nums_que_comencen_per(lista_nombres):
    contador = 0
    for nombre in lista_nombres:
        if nombre.startswith("a") or nombre.startswith("A"):
            contador += 1
    
    print("El numero de palabras que comienzan por la letra 'a' es: {}".format(contador))

nums_que_comencen_per(lista_nombres)

