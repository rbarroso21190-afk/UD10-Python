"""Escriure un programa on li passem un número (mínim 1 i màxim 900000) i ens indiqui la quantitat de dígits que té."""

numeroselec = int(input("Introduce un número entre 1 i 900000:"))

if numeroselec < 1 or numeroselec > 900000:
    print("El numero tiene que estar entre 1 y 900000")
else:
    numerotxt = str(numeroselec)
    cantidad_digitos = len(numerotxt)
    print("El numero {} tiene {} dígitos.".format(numeroselec, cantidad_digitos))