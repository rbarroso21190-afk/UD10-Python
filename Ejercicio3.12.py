"Definir una funció superposicio() que agafi dues llistes i retorni vertader si hi ha un element en comú, en cas contrari, que retorni fals."

lista1 = input("Introduce la primera lista con elementos separados por comas:").split(",")
lista2 = input("Introduce la segunda lista con elementos separados por comas:").split(",")
               

def superposicio(lista1, lista2):
    for element in lista1:
        if element in lista2:
            return True
        else:
            return False
        
if superposicio(lista1, lista2) == True:
    print("Las listas tienen elementos en común.")
else:
    print("Las listas no tienen elementos en común.")
    
