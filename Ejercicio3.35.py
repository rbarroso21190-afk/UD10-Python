"Escriure un programa que sumi els dígits d’un número donat i ens digui si la seva suma és parell o senar."

numero = int(input("Introduce un numero:"))
suma = 0
cadnum = str(numero)

for digito in cadnum:
    suma += int(digito)

if suma % 2 == 0:
    print("{} es par".format(suma))
else:
    print("{} es impar".format(suma))