"""Crear una funció que permeti llegir la informació d’un fitxer, 
però que controli que el fitxer existeix i que la seva obertura no doni cap problema. 
Fes-ho també utilitzant with. Si voleu podeu practicar el try, 
except afegint-ho a les funcions anteriors."""

def leer_fichero(nombre_fichero):
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            contenido = f.read()
            return contenido

    except FileNotFoundError:
        print("Error: el fichero no existe.")
        return None

    except PermissionError:
        print("Error: no tienes permisos para abrir este fichero.")
        return None

    except Exception as e:
        print("Se ha producido un error inesperado:", e)
        return None

nombre = input("Introduce el nombre del fichero que quieres leer:")
texto = leer_fichero(nombre)

if texto is not None:
    print("Contenido del fichero:")
    print(texto)
