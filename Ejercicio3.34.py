"Escriure un programa que imprimeixi la taula de multiplicar d’un número donat (mínim 1 màxim 20)."

numero = int(input("Introduce un numero entre 1 y 20:"))
x = [1,2,3,4,5,6,7,8,9,10]
if numero < 1 or numero > 20:
    print("El numero debe estar entre 1 y 20")
else:
    for x in range(1, 11):
        print("{} x {} = {}".format(numero, x, numero * x))

