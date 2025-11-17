"Definir una funció gran() que, donats dos números, retorni el major."

numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
mayor = 0

def gran(numero1, numero2, mayor):
    mayor = 0

    if numero1 > numero2:
        mayor = numero1
        print("El número mayor es:", mayor)
    else:
        mayor = numero2
        print("El número mayor es:", mayor)

gran(numero1, numero2, mayor)

