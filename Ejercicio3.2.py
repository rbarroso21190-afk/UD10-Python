edad = input("Introduce tu edad:")

print("Tienes {} años".format(edad))

if int(edad) > 18:
    print("Tienes mas de 18 años")
elif int(edad) == 18:
    print("Acabas de cumplir la mayoria de edad")
else:
    print("Eres menor de edad")

def mayoredad(edad):
    if int(edad) >= 18:
       print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    
edad = input("Introduce tu edad:")

mayoredad(edad)
