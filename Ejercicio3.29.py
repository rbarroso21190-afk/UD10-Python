"""Escriure un programa que demani dues paraules i ens digui si rimen o no. Rimen quan coincideixen les 3 darreres
lletres i rimen un poc quan coincideixen les 2 darreres, si no ens ha de dir que no rimen."""

palabra1 = input("introduce la primera palabra:")
palabra2 = input("introduce la segunda palabra:")

if palabra1[-3] == palabra2[-3]:
    print("\n{} y {} riman".format(palabra1, palabra2))
elif palabra1[-2] == palabra2[-2]:
    print("\n{} y {} riman un poco".format(palabra1, palabra2))
else:
    print("\n{} y {} no riman".format(palabra1, palabra2))
