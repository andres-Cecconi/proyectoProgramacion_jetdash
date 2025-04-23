# jetdash/menu.py
import pygame
import os
from recursos import cargar_imagen, cargar_musica

# Colores y fuentes
COLOR_TEXTO = (255, 255, 255)
COLOR_SELECCION = (100, 200, 255)
FONT_PATH = os.path.join("assets", "fonts", "PressStart2P-Regular.ttf")

# Menú principal con recursos centralizados
def mostrar_menu(pantalla):
    pygame.mixer.init()
    # Carga de assets
    imagen_fondo = cargar_imagen("menu_background.png")
    cargar_musica("menu_music.mp3")

    # Fuentes pixeladas para estética retro
    fuente_titulo   = pygame.font.Font(FONT_PATH, 60)
    fuente_opciones = pygame.font.Font(FONT_PATH, 18)

    opciones = ["Iniciar Juego", "Configuración", "Salir"]
    seleccion = 0
    reloj = pygame.time.Clock()

    while True:
        # Dibujar fondo y título
        pantalla.blit(pygame.transform.scale(imagen_fondo, pantalla.get_size()), (0, 0))
        titulo = fuente_titulo.render("JetDash", True, COLOR_TEXTO)
        pantalla.blit(
            titulo,
            (pantalla.get_width() // 2 - titulo.get_width() // 2, 100)
        )

        # Dibujar opciones
        for i, texto in enumerate(opciones):
            color = COLOR_SELECCION if i == seleccion else COLOR_TEXTO
            render = fuente_opciones.render(texto, True, color)
            pantalla.blit(
                render,
                (pantalla.get_width() // 2 - render.get_width() // 2, 220 + i * 50)
            )

        pygame.display.flip()

        # Manejador de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    elec = opciones[seleccion]
                    if elec == "Iniciar Juego":
                        return
                    elif elec == "Configuración":
                        from menu_config import mostrar_configuracion
                        mostrar_configuracion(pantalla)
                    elif elec == "Salir":
                        pygame.quit()
                        exit()

        reloj.tick(30)
