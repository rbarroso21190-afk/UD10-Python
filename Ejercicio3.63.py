"""Crear una classe anomenada Animal que tingui els següents atributs d’objecte: 
especie i edat i els següents mètodes: 
xerrar (abstracte), mourem (abstracte) i quisoc. 
Llavors, crearem diferents subclasses:  Cavall, Dofí, Abella, Humà, Centaure.... 
que hauran de redefinir aquestes mètodes. Crearem una nova subclasse d’Humà, anomenada Fiet. 
Llavors, crearem una subclasse Centaure que heredarà de Cavall i Humà. Finalment, 
tindrem una nova classe xou que no té cap relació amb els altres, 
però que té els mateixos mètodes que Animal implementats.
Ejercicio 3.63.2
Abella crearà un nou mètode anomenat, picar.
Ejercicio 3.63.3
Humà tindrà un nou atribut d’objecte anomenat, nom.
Ejercicio 3.63.4
Fiet tindrà un nou atribut d’objecte anomenat, pares (llista). I un nou mètode anomenat nompares que ens mostrarà el nom dels pares.
Ejercicio 3.63.5
Amb això, crear un llista d’elements de cada tipus i un for (bucle) que cridi als mètodes iguals."""

class Animal:
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print(f"Sóc un {self.especie} i tinc {self.edat} anys.")

class Cavall(Animal):
    def __init__(self, edat):
        # CAMBIO: Llamamos a Animal directamente para evitar conflictos
        Animal.__init__(self, "Cavall", edat)
    def xerrar(self):
        print("IIIIihhhhh!")
    def mourem(self):
        print("Galopo.")
class Dofí(Animal):
    def __init__(self, edat):
        Animal.__init__(self, "Dofí", edat)
    def xerrar(self):
        print("Iii-iii-iii!")
    def mourem(self):
        print("Nedo saltant.")
class Huma(Animal):
    def __init__(self, nom, edat):
        self.nom = nom
        # CAMBIO: Llamamos a Animal directamente
        Animal.__init__(self, "Humà", edat)
    def xerrar(self):
        print(f"Hola, soc {self.nom}.")
    def mourem(self):
        print("Camino.")
    def quisoc(self):
        print(f"Sóc un {self.especie}, em dic {self.nom} i tinc {self.edat} anys.")

# El resto de clases igual...
class Fiet(Huma):
    def __init__(self, nom, edat, pares):
        # Aquí sí podemos usar super() o Huma explicitamente
        Huma.__init__(self, nom, edat)
        self.pares = pares
    def nompares(self):
        print(f"Pares: {', '.join(self.pares)}")
    def xerrar(self):
        print("Gugu tata")

class Centaure(Huma, Cavall):
    def __init__(self, nom, edat):
        # Inicializamos manualmente para que todo cuadre
        Huma.__init__(self, nom, edat)
        self.especie = "Centaure"  # Sobreescribimos la especie
    
    def xerrar(self):
        print("Parlo i renillo.")
    def mourem(self):
        print("Galopo i camino.")

class Abella(Animal):
    def __init__(self, edat):
        Animal.__init__(self, "Abella", edat)
    def picar(self):
        print("Picada!")

class Xou:
    def xerrar(self):
        print("Xou!")
    def mourem(self):
        print("Moviment xou")
    def quisoc(self):
        print("Soc un Xou")

# --- PRUEBA ---
if __name__ == "__main__":
    print("\n=== 1. CREACIÓ D'OBJECTES ===")
    c = Cavall(10)
    d = Dofí(5)
    a = Abella(1)
    h = Huma("Laura", 35)
    f = Fiet("Biel", 2, ["Laura", "Marc"])
    cen = Centaure("Quiron", 500)
    x = Xou()

    print("Objectes creats correctament.")

    print("\n=== 2. PROVA DE MÈTODES ESPECÍFICS (Abella i Fiet) ===")
    print(f"L'abella té {a.edat} any i fa:")
    a.picar()
    
    print(f"El fiet es diu {f.nom} i:")
    f.nompares()

    print("\n=== 3. BUCLE POLIMÒRFIC (Tots junts) ===")
    # Lista con todos los tipos mezclados
    zoo = [c, d, a, h, f, cen, x]

    for ser in zoo:
        print("-" * 50)
        ser.quisoc()   # Todos saben decir quiénes son
        ser.xerrar()   # Todos saben hablar
        ser.mourem()   # Todos saben moverse
    
    print("-" * 50)