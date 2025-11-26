"""Definir una funció crear_llista_fitxer() on llegeixi un fitxer i transformi cada paraula 
llegida en un element de la llista. Prova-la."""

def crear_llista_fitxer(Fichero):
    with open(Fichero, "r", encoding="utf-8") as f:
        texto = f.read()
        lista = texto.split()
        return lista

resultado = crear_llista_fitxer("Frase.txt") 
print("Lista creada desde el fichero:")
print(resultado)


    
        