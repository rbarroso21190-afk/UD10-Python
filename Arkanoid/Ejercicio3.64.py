import pygame
import sys
import os

# --- INICIALIZACIÓN ---
pygame.init()

ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Arkanoid - Niveles de Dificultad")

FUENTE_TITULO = pygame.font.SysFont("Arial", 40, bold=True)
FUENTE_MENU = pygame.font.SysFont("Arial", 30)

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (50, 50, 255)
VERDE = (50, 255, 50)
ROJO = (255, 50, 50)
AMARILLO = (255, 255, 0)

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
        self.velocidad = velocidad_pala # La pala también corre más en niveles difíciles

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
        
        # DEFINICIÓN DE VELOCIDAD SEGÚN NIVEL
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

            # Rebotes paredes
            if self.rect.left <= 0:
                self.rect.left = 0
                self.vel_x *= -1
            if self.rect.right >= ANCHO:
                self.rect.right = ANCHO
                self.vel_x *= -1
            if self.rect.top <= 0:
                self.rect.top = 0
                self.vel_y *= -1
            
            # Perder
            if self.rect.bottom >= ALTO:
                return "muerto"
    
    def lanzar(self):
        self.activo = True
        # LANZAMIENTO RECTO (X = 0)
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

# --- FUNCIONES ---

def mostrar_menu_niveles():
    """Muestra el menú para elegir dificultad"""
    en_menu = True
    
    # Cargar Logo
    try:
        imagen_logo = pygame.image.load(RUTA_LOGO).convert_alpha()
        ancho_logo = 400
        alto_logo = int(imagen_logo.get_height() * (ancho_logo / imagen_logo.get_width()))
        imagen_logo = pygame.transform.scale(imagen_logo, (ancho_logo, alto_logo))
    except:
        imagen_logo = None

    # Opciones de menú
    opciones = ["Normal", "Difícil (x2)", "Hardcore (x3)"]
    seleccion = 0 # 0 = Normal, 1 = Dificil, 2 = Hardcore

    while en_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                # Navegar menú
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % 3
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % 3
                
                # Seleccionar
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                    # Devolvemos la velocidad base según la selección
                    if seleccion == 0: return 6   # Normal
                    if seleccion == 1: return 12  # Doble
                    if seleccion == 2: return 18  # Triple
                
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        # DIBUJAR MENÚ
        PANTALLA.fill(NEGRO)
        
        # Logo
        if imagen_logo:
            rect_logo = imagen_logo.get_rect(center=(ANCHO//2, 150))
            PANTALLA.blit(imagen_logo, rect_logo)
        else:
            txt = FUENTE_TITULO.render("ARKANOID", True, AZUL)
            PANTALLA.blit(txt, (ANCHO//2 - 100, 100))

        # Dibujar Opciones
        for i, opcion in enumerate(opciones):
            color = AMARILLO if i == seleccion else BLANCO
            texto = FUENTE_MENU.render(opcion, True, color)
            rect_texto = texto.get_rect(center=(ANCHO//2, 300 + i * 50))
            
            # Si está seleccionado, dibujamos flechas
            if i == seleccion:
                flecha = FUENTE_MENU.render("->", True, AMARILLO)
                PANTALLA.blit(flecha, (rect_texto.left - 40, rect_texto.top))
            
            PANTALLA.blit(texto, rect_texto)

        # Instrucciones pie de página
        pie = FUENTE_MENU.render("Usa FLECHAS y ESPACIO", True, AZUL)
        PANTALLA.blit(pie, (ANCHO//2 - 150, ALTO - 50))

        pygame.display.flip()
        reloj.tick(60)

def juego_principal(velocidad_juego):
    sprites = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    # Ajustamos velocidad de la pala para que sea jugable en Hardcore
    # Si la bola va x3, la pala debe ir más rápido también
    velocidad_pala = 8 + (velocidad_juego / 2) 

    nave = Nave(velocidad_pala)
    bola = Bola(velocidad_juego) # Pasamos la velocidad elegida
    sprites.add(nave)
    sprites.add(bola)

    for fila in range(5):
        for col in range(10):
            b = Bloque(50 + col * 70, 50 + fila * 30)
            sprites.add(b)
            bloques.add(b)

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
                    jugando = False # Vuelve al menú

        nave.update()
        estado = bola.update(nave)

        if estado == "muerto":
            bola.activo = False
            bola.vel_x = 0
            bola.vel_y = 0
            bola.rect.midbottom = nave.rect.midtop

        # REBOTE PALA (CONTROL DE ÁNGULO)
        if pygame.sprite.collide_rect(bola, nave) and bola.vel_y > 0:
            # Calculamos ángulo basado en dónde golpea
            diferencia_x = bola.rect.centerx - nave.rect.centerx
            ancho_nave = nave.rect.width / 2
            offset = diferencia_x / ancho_nave
            
            # Ajuste de rebote
            angulo_maximo = 10 # Más ángulo para niveles rápidos
            bola.vel_x = offset * angulo_maximo
            bola.vel_y = -bola.velocidad_base

        # REBOTE BLOQUES
        impactos = pygame.sprite.spritecollide(bola, bloques, True)
        if impactos:
            bola.vel_y *= -1
            
        if len(bloques) == 0:
            # Pantalla de victoria simple en consola
            print("¡NIVEL COMPLETADO!")
            jugando = False

        PANTALLA.fill(NEGRO)
        sprites.draw(PANTALLA)
        
        # Mostrar nivel actual en pantalla
        nivel_txt = f"Vel: {velocidad_juego}"
        txt_surface = pygame.font.SysFont("Arial", 16).render(nivel_txt, True, BLANCO)
        PANTALLA.blit(txt_surface, (10, ALTO - 20))

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    while True:
        # 1. El menú devuelve la velocidad seleccionada
        velocidad_seleccionada = mostrar_menu_niveles()
        
        # 2. Iniciamos el juego con esa velocidad
        juego_principal(velocidad_seleccionada)