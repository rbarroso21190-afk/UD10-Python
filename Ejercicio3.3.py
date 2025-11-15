numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo número:"))

print("Selecciona 1 para operacion entera o 2 para operacion en coma flotante:")
decision = int(input("(1/2):"))

if decision == 1:

    numero1 = int(numero1)
    numero2 = int(numero2)

    print("Seleciona la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponente")
    print("7. Division entera")

    operacion = int(input("Ingresa el numero de la operacion (1/2/3/4/5/6/7):"))

    if operacion == 1:
        print("El resultado de la suma es:", numero1 + numero2)
    elif operacion == 2:
        print("El resultado de la resta es:", numero1 - numero2)
    elif operacion == 3:
        print("El resultado de la multiplicacion es:", numero1 * numero2)
    elif operacion == 4:
        print("El resultado de la division es:", numero1 / numero2)
    elif operacion == 5:
        print("El resultado del modulo es:", numero1 % numero2)
    elif operacion == 6:
        print("El resultado del exponente es:", numero1 ** numero2)
    elif operacion == 7:
        print("El resultado de la division entera es:", numero1 // numero2)
    else:
        print("Operacion no valida.")

elif decision == 2:

    print("Seleciona la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponente")

    operacion = int(input("Ingresa el numero de la operacion (1/2/3/4/5/6):"))

    if operacion == 1:
        print("El resultado de la suma es:", numero1 + numero2)
    elif operacion == 2:
        print("El resultado de la resta es:", numero1 - numero2)
    elif operacion == 3:
        print("El resultado de la multiplicacion es:", numero1 * numero2)
    elif operacion == 4:
        print("El resultado de la division es:", numero1 / numero2)
    elif operacion == 5:
        print("El resultado del modulo es:", numero1 % numero2)
    elif operacion == 6:
        print("El resultado del exponente es:", numero1 ** numero2)
    else:
        print("Operacion no valida.")
else:
    print("Decision no valida.")
