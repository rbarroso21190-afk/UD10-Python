"Escriure un programa que sumi tots els números entre dos números donats, ambdós inclosos."

numero1 = int(input("Ingresa el primer numero:"))
numero2 = int(input("Ingresa el segundo numero:"))

suma = 0

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

while numero1 <= numero2:
    suma += numero1
    numero1 += 1    

print("La suma es:", suma)
