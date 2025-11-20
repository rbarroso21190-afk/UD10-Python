"""Escriure un programa que si li introduïm un número menor de 100, 
mostri la suma dels quadrats dels números que estan separats entre sí per a quatres posicions. 
Ex: 80 --> 76**2 + 72**2 + 68**2 + ... """

numero = int(input("Introduce un numero menor de 100:"))

if 0 < numero < 100:
    suma = 0
    serie = list(range(numero, 0, -4))
    
    print("La serie de cuadrados es: ", end="")
    
    for indice, i in enumerate(serie):
        suma += i**2  
        print(f"{i}**2", end="")
        
        if indice < len(serie) - 1:
            print(" + ", end="")  
                   
    print("\n\nLa suma de los cuadrados restando 4 posiciones es: {}".format(suma))

else:
    print("El número introducido no es válido (debe ser > 0 y < 100).")
