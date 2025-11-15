"Afegeix, a la calculadora anterior, una nova funcionalitat que permeti treballar amb canvis de base (bin, octal, decimal, hexadecimal)."

print("Selecciona 1 para operacion entera, 2 para operacion en coma flotante o 3 para cambio de base:")
decision = int(input("(1/2/3):"))

if decision == 1:

    numero1 = int(input("Ingrese el primer número:"))
    numero2 = int(input("Ingrese el segundo número:"))

    print("\nSeleciona la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponente")
    print("7. Division entera\n")

    operacion = int(input("Ingresa el numero de la operacion (1/2/3/4/5/6/7):"))

    if operacion == 1:
        print("\nEl resultado de la suma es:", numero1 + numero2)
    elif operacion == 2:
        print("\nEl resultado de la resta es:", numero1 - numero2)
    elif operacion == 3:
        print("\nEl resultado de la multiplicacion es:", numero1 * numero2)
    elif operacion == 4:
        print("\nEl resultado de la division es:", numero1 / numero2)
    elif operacion == 5:
        print("\nEl resultado del modulo es:", numero1 % numero2)
    elif operacion == 6:
        print("\nEl resultado del exponente es:", numero1 ** numero2)
    elif operacion == 7:
        print("\nEl resultado de la division entera es:", numero1 // numero2)
    else:
        print("\nOperacion no valida.")

elif decision == 2:

    numero1 = float(input("Ingrese el primer número:"))
    numero2 = float(input("Ingrese el segundo número:"))

    print("\nSeleciona la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponente")

    operacion = int(input("Ingresa el numero de la operacion (1/2/3/4/5/6):"))

    if operacion == 1:
        print("\nEl resultado de la suma es:", numero1 + numero2)
    elif operacion == 2:
        print("\nEl resultado de la resta es:", numero1 - numero2)
    elif operacion == 3:
        print("\nEl resultado de la multiplicacion es:", numero1 * numero2)
    elif operacion == 4:
        print("\nEl resultado de la division es:", numero1 / numero2)
    elif operacion == 5:
        print("\nEl resultado del modulo es:", numero1 % numero2)
    elif operacion == 6:
        print("\nEl resultado del exponente es:", numero1 ** numero2)
    else:
        print("\nOperacion no valida.")

elif decision == 3:

    numero = input("Ingrese un número entero para cambiar de base:")

    print("\nSeleciona la base del número ingresado:")
    print("1. Binario")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal\n")

    base = int(input("Ingresa el numero de la base (1/2/3/4):"))

    if base == 1:
        numero = int(str(numero), 2)
    elif base == 2:
        numero = int(str(numero), 8)
    elif base == 3:
        numero = int(numero)
    elif base == 4:
        numero = int(str(numero), 16)
    else:
        print("Base no valida.")
        
    
    print("\nSeleciona la base a la que deseas convertir:")
    print("1. Binario")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal\n")

    base2 = int(input("Ingresa el numero de la base (1/2/3/4):"))
    
    if base2 == 1:
        print("\nEl número en binario es:", bin(numero))
    elif base2 == 2:
        print("\nEl número en octal es:", oct(numero))
    elif base2 == 3:
        print("\nEl número en decimal es:", numero)
    elif base2 == 4:
        print("\nEl número en hexadecimal es:", hex(numero))
    else:
        print("\nBase no valida.")
else:
    print("\nDecision no valida.")
