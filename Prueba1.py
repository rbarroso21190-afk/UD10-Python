a = float(input("Escribe el primer numero:"))
b = float(input("Escribe el segundo numero:"))
c = float(input("Escribe el tercer numero:"))

d = a + b + c

print("El resultado de la suma {} + {} + {} es: {}".format(a, b, c, d))

if d > 20:
    print("La suma es mayor que 20, que es: {}".format(d))
else:
    print("La suma es menor o igual a 20, que es: {}".format(d))

d = a * b * c

print("El resultado de la multiplicacion {} * {} * {} es: {}".format(a, b, c, d))

if d > 100:
    print("La suma es mayor que 100, que es: {}".format(d))
else:
    print("La suma es menor o igual a 100, que es: {}".format(d))