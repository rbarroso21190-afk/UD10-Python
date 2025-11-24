"Escriure un programa que mostri els dígits parells d’un número donat."

numero = int(input("Introduce un numero:"))
strnum = str(numero)

for digito in strnum:
    digitoint = int(digito)
    if digitoint % 2 == 0:
        print("{} es par".format(digitoint))
    else:
        print("{} es impar".format(digitoint))
    
