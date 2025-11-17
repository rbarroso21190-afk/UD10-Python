"Definir una funció que calculi la longitud d’una llista o d’una cadena donada. Prova-la amb diferents exemples."

def l_c():
    print("1.Para lista")
    print("2.Para cadena")
    eleccion = int(input("Elige una opcion (1/2):"))

    if eleccion == 1:
        lista = input("Introduce una lista de elementos separados por comas: ").split(',')
        print("La longitud de la lista es:", len(lista))
    elif eleccion == 2:
        cadena = input("Introduce una cadena de texto: ")
        print("La longitud de la cadena es:", len(cadena))
    else:
        print("Opcion no valida.")
    
l_c()

def li_ca():
    print("1.Para lista")
    print("2.Para cadena")
    eleccion = int(input("Elige una opcion (1/2):"))

    for eleccion in range(1,3):
        if eleccion == 1:
            lista = input("Introduce una lista de elementos separados por comas: ").split(',')
            print("La longitud de la lista es:", len(lista))
            break
        elif eleccion == 2:
            cadena = input("Introduce una cadena de texto: ")
            print("La longitud de la cadena es:", len(cadena))
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")
            break

li_ca()
    