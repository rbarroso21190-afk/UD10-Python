"Definir una funció invertir() que calculi la inversa d’una cadena. Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS."

def invertir(cadena):
    return cadena[::-1]   #cadena[inicio:fin:sentido]

entrada = input("Introduce una cadena de texto:")

print("La cadena invertida es:", invertir(entrada))