"Crear el joc d’arkanoid utilitzant la llibreria pygame."

import pygame
import sys
import os

# --- INICIALIZACIÓN ---
pygame.init()

ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Arkanoid - Final Version")

# Fuentes
FUENTE_TITULO = pygame.font.SysFont("Arial", 50, bold=True)
FUENTE_MENU = pygame.font.SysFont("Arial", 30)
FUENTE_GUI = pygame.font.SysFont("Arial", 24, bold=True) # Para vidas y puntos

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (50, 50, 255)
VERDE = (50, 255, 50)
ROJO = (255, 50, 50)
AMARILLO = (255, 255, 0)
GRIS = (100, 100, 100)

reloj = pygame.time.Clock()

# --- RUTAS ---
RUTA_CARPETA = "/home/ciclesraulbarroso/Documentos/AO/UD10-Python/Arkanoid/Imagenes"
RUTA_LOGO = os.path.join(RUTA_CARPETA, "Arkanoidlogo.png")
RUTA_PALA = os.path.join(RUTA_CARPETA, "pala.svg")
RUTA_BOLA = os.path.join(RUTA_CARPETA, "bola.svg")
RUTA_LADRILLO = os.path.join(RUTA_CARPETA, "ladrillo.svg")

# --- CLASES ---

class Nave(pygame.sprite.Sprite):
    def __init__(self, velocidad_pala):
        super().__init__()
        try:
            img = pygame.image.load(RUTA_PALA).convert_alpha()
            self.image = pygame.transform.scale(img, (100, 20))
        except:
            self.image = pygame.Surface((100, 20))
            self.image.fill(AZUL)
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO // 2, ALTO - 20)
        self.velocidad = velocidad_pala

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > ANCHO: self.rect.right = ANCHO

class Bola(pygame.sprite.Sprite):
    def __init__(self, velocidad_nivel):
        super().__init__()
        try:
            img = pygame.image.load(RUTA_BOLA).convert_alpha()
            self.image = pygame.transform.scale(img, (20, 20))
        except:
            self.image = pygame.Surface((20, 20))
            self.image.fill(BLANCO)
            
        self.rect = self.image.get_rect()
        self.velocidad_base = velocidad_nivel
        self.vel_x = 0
        self.vel_y = 0
        self.activo = False 

    def update(self, nave):
        if not self.activo:
            self.rect.midbottom = nave.rect.midtop
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            if self.rect.left <= 0:
                self.rect.left = 0
                self.vel_x *= -1
            if self.rect.right >= ANCHO:
                self.rect.right = ANCHO
                self.vel_x *= -1
            if self.rect.top <= 0:
                self.rect.top = 0
                self.vel_y *= -1
            
            # Condición de Muerte
            if self.rect.bottom >= ALTO:
                return "muerto"
    
    def lanzar(self):
        self.activo = True
        self.vel_x = 0  
        self.vel_y = -self.velocidad_base

class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            img = pygame.image.load(RUTA_LADRILLO).convert_alpha()
            self.image = pygame.transform.scale(img, (60, 20))
        except:
            self.image = pygame.Surface((60, 20))
            self.image.fill(VERDE)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# --- FUNCIONES DE PANTALLA ---

def mostrar_menu_niveles():
    """Menú principal para elegir dificultad"""
    en_menu = True
    try:
        imagen_logo = pygame.image.load(RUTA_LOGO).convert_alpha()
        ancho_logo = 400
        alto_logo = int(imagen_logo.get_height() * (ancho_logo / imagen_logo.get_width()))
        imagen_logo = pygame.transform.scale(imagen_logo, (ancho_logo, alto_logo))
    except:
        imagen_logo = None

    opciones = ["Normal", "Difícil (x2)", "Hardcore (x3)"]
    seleccion = 0

    while en_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP: seleccion = (seleccion - 1) % 3
                if evento.key == pygame.K_DOWN: seleccion = (seleccion + 1) % 3
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                    if seleccion == 0: return 6
                    if seleccion == 1: return 12
                    if seleccion == 2: return 18
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        PANTALLA.fill(NEGRO)
        if imagen_logo:
            PANTALLA.blit(imagen_logo, imagen_logo.get_rect(center=(ANCHO//2, 150)))
        else:
            txt = FUENTE_TITULO.render("ARKANOID", True, AZUL)
            PANTALLA.blit(txt, (ANCHO//2 - 100, 100))

        for i, opcion in enumerate(opciones):
            color = AMARILLO if i == seleccion else BLANCO
            texto = FUENTE_MENU.render(opcion, True, color)
            rect_texto = texto.get_rect(center=(ANCHO//2, 300 + i * 50))
            if i == seleccion:
                flecha = FUENTE_MENU.render("->", True, AMARILLO)
                PANTALLA.blit(flecha, (rect_texto.left - 40, rect_texto.top))
            PANTALLA.blit(texto, rect_texto)

        pie = FUENTE_MENU.render("Usa FLECHAS y ENTER", True, AZUL)
        PANTALLA.blit(pie, (ANCHO//2 - 150, ALTO - 50))
        pygame.display.flip()
        reloj.tick(60)

def pantalla_game_over(puntos, victoria=False):
    """Pantalla final de juego"""
    esperando = True
    
    # Textos
    if victoria:
        titulo = FUENTE_TITULO.render("¡VICTORIA!", True, VERDE)
    else:
        titulo = FUENTE_TITULO.render("GAME OVER", True, ROJO)
        
    puntos_txt = FUENTE_MENU.render(f"Puntuación Final: {puntos}", True, BLANCO)
    info1 = FUENTE_MENU.render("Pulsa ESPACIO para Menú", True, GRIS)
    info2 = FUENTE_MENU.render("Pulsa ESC para Salir", True, GRIS)

    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False # Vuelve al bucle principal
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        PANTALLA.fill(NEGRO)
        
        # Centrar textos
        rect_titulo = titulo.get_rect(center=(ANCHO//2, ALTO//2 - 60))
        rect_puntos = puntos_txt.get_rect(center=(ANCHO//2, ALTO//2))
        rect_info1 = info1.get_rect(center=(ANCHO//2, ALTO//2 + 60))
        rect_info2 = info2.get_rect(center=(ANCHO//2, ALTO//2 + 100))

        PANTALLA.blit(titulo, rect_titulo)
        PANTALLA.blit(puntos_txt, rect_puntos)
        PANTALLA.blit(info1, rect_info1)
        PANTALLA.blit(info2, rect_info2)

        pygame.display.flip()
        reloj.tick(60)

def juego_principal(velocidad_juego):
    sprites = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    velocidad_pala = 8 + (velocidad_juego / 2)
    nave = Nave(velocidad_pala)
    bola = Bola(velocidad_juego)
    sprites.add(nave)
    sprites.add(bola)

    for fila in range(5):
        for col in range(10):
            b = Bloque(50 + col * 70, 50 + fila * 30)
            sprites.add(b)
            bloques.add(b)

    # VARIABLES DE ESTADO
    vidas = 3
    puntos = 0
    jugando = True
    
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not bola.activo:
                    bola.lanzar()
                if evento.key == pygame.K_ESCAPE:
                    jugando = False # Salir al menú

        nave.update()
        estado = bola.update(nave)

        # --- SISTEMA DE VIDAS ---
        if estado == "muerto":
            vidas -= 1
            if vidas == 0:
                # Se acabaron las vidas -> GAME OVER
                pantalla_game_over(puntos, victoria=False)
                jugando = False # Rompe el bucle para volver al menú
            else:
                # Perder una vida pero seguir jugando
                bola.activo = False
                bola.vel_x = 0
                bola.vel_y = 0
                bola.rect.midbottom = nave.rect.midtop
                # Opcional: Sonido de perder vida aquí

        # Rebotes Nave
        if pygame.sprite.collide_rect(bola, nave) and bola.vel_y > 0:
            diferencia_x = bola.rect.centerx - nave.rect.centerx
            ancho_nave = nave.rect.width / 2
            offset = diferencia_x / ancho_nave
            bola.vel_x = offset * 10
            bola.vel_y = -bola.velocidad_base

        # Rebotes Bloques
        impactos = pygame.sprite.spritecollide(bola, bloques, True)
        if impactos:
            bola.vel_y *= -1
            puntos += 10 * len(impactos) # Sumar puntos
            
        # Condición de Victoria
        if len(bloques) == 0:
            pantalla_game_over(puntos, victoria=True)
            jugando = False

        # --- DIBUJADO ---
        PANTALLA.fill(NEGRO)
        sprites.draw(PANTALLA)

        # Interfaz (HUD)
        txt_vidas = FUENTE_GUI.render(f"Vidas: {vidas}", True, ROJO)
        txt_puntos = FUENTE_GUI.render(f"Puntos: {puntos}", True, BLANCO)
        
        PANTALLA.blit(txt_vidas, (10, ALTO - 30))
        PANTALLA.blit(txt_puntos, (ANCHO - 150, ALTO - 30))

        pygame.display.flip()
        reloj.tick(60)

# --- BUCLE PRINCIPAL DE LA APLICACIÓN ---
if __name__ == "__main__":
    while True:
        velocidad = mostrar_menu_niveles() # 1. Elegir Nivel
        juego_principal(velocidad)         # 2. Jugar -> Game Over -> Vuelve aquí