"Escriure un programa que converteixi el números binaris en enters."

sbin = (input("introduce un numero binario:"))

def conversor(sbin):
    for a in str(sbin):
        if a != "0" and a != "1":
            print("El numero introducido no es binario")
            break
        else:
            dec = int(sbin, 2)
            print("El numero en decimal es:", dec)

conversor(sbin)
