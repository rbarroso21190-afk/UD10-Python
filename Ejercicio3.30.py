"""Escriure un programa que calculi en quan s'hauria convertit el nostre capital al final dels anys. 
Per això li hem de demanar a l’usuari que introdueixi la quantitat a sol·licitar (mínim 50000€ màxim 800000€), 
un interès (mínim 0.5% i màxim 13%) i el número d’anys (mínim 3 anys - màxim 40 anys).  
La fórmula per calcular-ho és: Cfinal = Cinicial * (1 + interés/100) **  anys.  
Ex. 10000€ a 4.5% d’interés a 20 anys s’ha de convertir en 24117.14€"""

solicitud = float(input("Introduce la cantidad de dinero, entre 50000€ y 800000€:"))

if solicitud < 50000 or solicitud > 800000:
    print("Cantidad no válida. Debe estar entre 50000€ y 800000€")
else:
    interes = float(input("Introduce el interés, entre 0.5% y 13%:"))
    if interes < 0.5 or interes > 13:
        print("Interes no valido, debe estar entre 0.5% y 13%")
    else:
        años = int(input("Introduce el número de años, entre 3 y 40:"))
        if años < 3 or años > 40:
            print("Numero de años no válido, debe estar entre 3 y 40")
        else:
            Cfinal = solicitud * (1 + interes / 100) ** años
            print(f"El capital final después de {años} años será: {Cfinal:.2f}€")