"""Escriure un programa on donats l’any actual, i l’any de naixement i el nom de 4 persones, 
calculi els anys que farà cada un d’ells l’any actual i imprimeixi totes les dades tabulades per pantalla. 
Ex:
Any actual 2022
Nom			Data naixement	Anys que farà aquest any
Pere			2000			22
Maria			1999			23
Anna			2005			17
"""

año_act = int(input("Introduce el año actual:"))
x = []
y = []
z = []

for a in range(4):
    nombre = input("Introduce el nombre de la persona:")
    año_nac = int(input("En que año nacio {}?: ".format(nombre)))
    años_que_hara = año_act - año_nac

    x.append(nombre)
    y.append(año_nac)
    z.append(años_que_hara)

print("\nAño actual {}".format(año_act))
print("Nombre\t\tAño de nacimiento\tAños que hará este año")

for a in range(4):
    print("{}\t\t{}\t\t\t{}".format(x[a], y[a], z[a]))