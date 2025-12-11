import random
import os

# --- 1. LLISTES I ALEATORIS ---
def app_llistes():
    print("\n--- 1. Llistes ---")
    # Generem 5 números aleatoris del 1 al 20 en una sola línia
    llista = [random.randint(1, 20) for _ in range(5)]
    
    print(f"Llista original: {llista}")
    llista.sort()
    print(f"Ordenada:      {llista}")
    print(f"El més gran és el {max(llista)} i el petit el {min(llista)}")

# --- 2. FITXERS (Agenda Simple) ---
def app_fitxers():
    print("\n--- 2. Agenda (Fitxers) ---")
    opcio = input("Vols (L)legir o (E)scriure? ").lower()
    
    if opcio == 'e':
        text = input("Què vols guardar a l'agenda? ")
        with open("agenda.txt", "a") as f:
            f.write(text + "\n")
        print("Guardat!")
    elif opcio == 'l':
        if os.path.exists("agenda.txt"):
            with open("agenda.txt", "r") as f:
                print("\n--- La teva agenda ---")
                print(f.read())
        else:
            print("No hi ha cap fitxer encara.")

# --- 3. JOC (Endevina el número) ---
def app_joc():
    print("\n--- 3. Joc: Endevina el número (1-10) ---")
    secret = random.randint(1, 10)
    intents = 3
    
    while intents > 0:
        try:
            num = int(input(f"Et queden {intents} vides. Quin número és? "))
            if num == secret:
                print("🎉 Has guanyat! L'has encertat.")
                return
            else:
                print("Incorrecte...")
                intents -= 1
        except:
            print("Escriu un número vàlid!")
            
    print(f"Has perdut. Era el {secret}.")

# --- 4. OBJECTES (Classe Persona) ---
def app_poo():
    print("\n--- 4. Objectes i Herència ---")
    
    # Classe Pare
    class Persona:
        def __init__(self, nom):
            self.nom = nom
        def saludar(self):
            return f"Hola, soc {self.nom}"

    # Classe Filla (Herència)
    class Alumne(Persona):
        def estudiar(self):
            return "Estic estudiant Python 🐍"

    # Utilitzem els objectes
    profe = Persona("Pep")
    jo = Alumne("Raül")
    
    print(profe.saludar())           # Mètode del pare
    print(jo.saludar())              # L'alumne també saluda (herència)
    print(f"{jo.nom} diu: {jo.estudiar()}") # Mètode propi

# --- 5. BIG DATA (Pandas) ---
def app_bigdata():
    print("\n--- 5. Dades amb Pandas ---")
    try:
        import pandas as pd
        data = {
            'Nom': ['Ana', 'Pol', 'Clara'],
            'Edat': [25, 18, 30],
            'Ciutat': ['BCN', 'MAD', 'VAL']
        }
        df = pd.DataFrame(data)
        print("Taula de dades:")
        print(df)
        print("\nNomés els majors de 20 anys:")
        print(df[df['Edat'] > 20])
    except:
        print("Error: Instal·la pandas amb 'pip install pandas'")

# --- 6. WEB (Flask) ---
def app_web():
    print("\n--- 6. Web Server ---")
    print("Obre http://127.0.0.1:5000 al teu navegador.")
    print("Prem Ctrl+C a la terminal per aturar-lo.")
    try:
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def inici():
            return "<h1>Hola món!</h1><p>Això és un servidor Python.</p>"

        app.run(port=5000)
    except:
        print("Error: Instal·la flask amb 'pip install flask'")

# --- MENÚ PRINCIPAL ---
def menu():
    funcions = {
        "1": app_llistes,
        "2": app_fitxers,
        "3": app_joc,
        "4": app_poo,
        "5": app_bigdata,
        "6": app_web
    }

    while True:
        print("\n=== MENÚ PROJECTE ===")
        print("1. Llistes | 2. Fitxers | 3. Joc")
        print("4. Objectes| 5. Pandas  | 6. Web")
        print("0. Sortir")
        
        opcio = input("Tria una opció: ")
        
        if opcio == "0": break
        elif opcio in funcions:
            funcions[opcio]() # Executa la funció seleccionada
        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    menu()