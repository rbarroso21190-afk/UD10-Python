"""Escriure un programa que ens permeti jugar a una versió simplificada del joc de MasterMind, 
el joc consisteix en crear un codi de 4 xifres i demanar a l’usuari que vagi introduint codis de 4 xifres fins que l’endevini. 
En cada jugada, li direm quants número ha encertat (estan en la posició correcte) 
i quants coincideixen (i són, però no estan en la posició correcte)."""

import random
from collections import Counter  #Esto cuenta cuántas veces aparece cada dígito

codigo = [random.randint(0, 9) for _ in range(4)]
solucion = ''.join(str(x) for x in codigo)

print("Juego MasterMind simplificado.")
print("Intenta adivinar el codigo de 4 cifras!\n")

while True:
    intento = input("Introduce un codigo de 4 cifras:")

    if len(intento) != 4 or not intento.isdigit():
        print("Error: introduce EXACTAMENTE 4 cifras.\n")
        continue

    intento = [int(x) for x in intento]

    aciertos_posicion = sum(1 for a, b in zip(intento, codigo) if a == b) #a:número del intento, b:número del código correcto
                                                                          #zip empareja elementos de dos (o más) listas, uno por uno, según su posición
    contador_codigo = Counter(codigo)
    contador_intento = Counter(intento)

    coincidencias = sum(min(contador_codigo[d], contador_intento[d]) for d in contador_codigo) 
    coincidencias -= aciertos_posicion

    if aciertos_posicion == 4:
        print("Has ganado! El codigo era: {}".format(solucion))
        break

    print(f"Has acertado {aciertos_posicion} en la posicion correcta.")
    print(f"Hay {coincidencias} cifras correctas pero en posicion incorrecta.\n")
