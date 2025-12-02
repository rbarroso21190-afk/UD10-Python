"Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho."

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
        return None

print(dividir(10, 2))   
print(dividir(10, 0))   