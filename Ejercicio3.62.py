"""Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori, 
a dins, crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe. Tancar el fitxer. 
Obrir-lo per afegir el nom dels professors. Tancar-lo. Finalment, 
l’obrirem i posarem tot el seu contingut dins una llista de noms."""

import os

# --- PASO 1: Configurar las rutas ---

# Detectamos dónde estamos (ej: .../AO/UD10-Python)
ruta_donde_estoy = os.getcwd()

# Obtenemos el directorio PADRE (subimos un nivel atrás)
# Esto nos llevará de 'UD10-Python' a 'AO'
ruta_anterior = os.path.dirname(ruta_donde_estoy)

# Definimos la ruta de la nueva carpeta dentro de 'AO'
nombre_carpeta = "Prova"
ruta_destino = os.path.join(ruta_anterior, nombre_carpeta)

# Definimos la ruta completa del archivo dentro de esa nueva carpeta
ruta_archivo_completa = os.path.join(ruta_destino, "Ex12.txt")

print(f"Ruta actual del script: {ruta_donde_estoy}")
print(f"Vamos a crear la carpeta en: {ruta_destino}")

# --- PASO 2: Crear el directorio ---
# Esto creará 'Prova' dentro de 'AO'
os.makedirs(ruta_destino, exist_ok=True)


# --- PASO 3: Listas de datos ---
alumnos = [
    "IKER ANDRES ENSEÑAT", "YOUSSEF AZANAI", "OSAMA EL HAJOUI EL HAJOUI",
    "MOHAMED EL MAKADMI LAMKADEM", "POL FORNES CABRERA", "LUCA GELMETTI",
    "JOAN GÓMEZ CARRERAS", "IZAN GÓMEZ FERRO", "IKER HEREDIA HEREDIA",
    "AITOR HOLGADO HARTO", "MOHAMED MAMOUNI KASMI", "DANIEL MANTECA GARRIGA",
    "JUSTIN AARON MONTIEL CANCHINGRE", "RAFEL PASCUAL PONS", "EDGAR PELEGRÍ HITA",
    "IZAN PONS PONS", "CIRO FABIAN SALAS CARBALLO", "LUCAS SANTANA PREVI",
    "ARITZ SEGUÍ TALTAVULL", "RAUL SINTES RUIZ", "IAN SINTES SEGUI",
    "RUSSELL MIJAEL VÁSQUEZ CHURA"
]

profesores = [
    "Joan Carreras Vinent", "BELEN CABRERA LORENZO", "David Labiano Boutens",
    "IRENE COLL SERRA", "Pep Malle", "Catalina Peñalver Anglada",
    "MANEL BOSCH MONJO", "JESÚS CAPÓ PONS"
]

# --- PASO 4: Escribir y Modificar ---

# 1. Crear y escribir alumnos (Modo 'w')
with open(ruta_archivo_completa, "w", encoding="utf-8") as f:
    f.write("--- ALUMNOS ---\n")
    for alumno in alumnos:
        f.write(alumno + "\n")

# 2. Añadir profesores (Modo 'a')
with open(ruta_archivo_completa, "a", encoding="utf-8") as f:
    f.write("\n--- PROFESORES ---\n")
    for profe in profesores:
        f.write(profe + "\n")

# --- PASO 5: Comprobación ---
if os.path.exists(ruta_archivo_completa):
    print(f"\n¡LISTO! Archivo creado en: {ruta_archivo_completa}")
else:
    print("Algo ha fallado.")