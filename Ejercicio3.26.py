"""Definir una funció es_de_traspas() donat un any, ens indiqui si és de traspàs o no. 
Un any és de traspàs si és divisible per 4, però no per 100 i també és divisible per 400."""

año = int(input("Introduce un año:"))

def es_de_traspas(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("{} es un año de traspaso".format(año))
    else:
        print("{} no es un año de traspaso".format(año))

es_de_traspas(año)
        