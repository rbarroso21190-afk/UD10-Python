"Escriu un programa que ens indiqui tots els números primers entre 1 i 100 i ens digui quants n’hi ha."

for x in range(1, 100):
    primo = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            primo = False
            break
    if primo:
        print(x)
