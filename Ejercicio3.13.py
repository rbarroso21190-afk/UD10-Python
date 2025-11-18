"""Definir una funció crear_repetits() que agafi un número enter i un caràcter i retorni el caràcter multiplicat pel número enter. 
Ex: crear_repetits(5, “a”), retorni “aaaaa”"""

num = int(input("Introduce un número entero:"))
char = input("Introduce un carácter:")

def crear_repetits(num, char):
    return char * num

print(crear_repetits(num, char))