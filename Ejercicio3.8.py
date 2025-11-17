"Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. Prova-la amb diferents exemples."

caracter = ""

def es_vocal(caracter):
    caracter = input("Introduce un caracter:")
    vocal = "aeiouAEIOU"
    if caracter in vocal and len(caracter):
        print("True")
    else:
        print("False")
    
es_vocal(caracter)

def si_vocal(caracter):
    caracter = input("Introduce un caracter:")
    for char in caracter:
        if char in "aeiouAEIOU":
            print("True")
            break
        else:
            print("False")
            break
        
si_vocal(caracter)