"""Crear una funció que donada una llista de paraules i una lletra, 
retorni una llista amb les paraules que comencen per la lletra donada. Utilitzar filter. 
Ex: [“maria”, “manta”, “peu”, “mà”] i li deim que ens retorni totes les que comencen per ‘p’, 
en retorni [‘peu’]."""

abecedario = [
    "Amanecer","Barco","Casa","Dado",    
    "Elefante", "Flor","Gato","Hielo",
    "Isla","Jarabe","Kilo","Luna",
    "Mar", "Nube","Oso","Perro",
    "Queso", "Río","Sol", "Tierra",
    "Uva","Vela","Waffle", "Xilófono",
    "Yate", "Zorro"
]

def autocompletar(letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), abecedario))

letra = input("Introduce una letra:")
resultado = autocompletar(letra)
print(resultado)
    