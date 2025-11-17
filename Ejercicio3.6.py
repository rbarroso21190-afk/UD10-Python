"Definir una funció gran_de_tres(), donats tres números, retorni el major. Prova-la amb diferents exemples."

numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
numero3 = int(input("Ingrese el tercer número:"))

def gran_de_tres(a, b, c):
    if a > b and a > c:
        print("El mayor es:", a)
    elif b > a and b > c:
        print("El mayor es:", b)
    else:
        print("El mayor es:", c)

gran_de_tres(numero1, numero2, numero3)

a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))
c = int(input("Ingrese el tercer número:"))

def grande_de_tres(a, b, c):
    numero = 0
    while numero < a or numero < b or numero < c:
        numero += 1 
    return numero

print("El mayor es:", grande_de_tres(a, b, c))