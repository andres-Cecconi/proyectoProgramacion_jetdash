# jetdash/menu_config.py
import pygame
import os
from recursos import cargar_imagen

# Colores y fuentes\
COLOR_TEXTO = (255, 255, 255)
COLOR_SELECCION = (100, 200, 255)
FONT_PATH = os.path.join("assets", "fonts", "PressStart2P-Regular.ttf")

# Submenú de configuración de audio
def mostrar_configuracion(pantalla):
    pygame.mixer.init()
    # Carga de fondo desde recursos
    imagen_fondo = cargar_imagen("menu_background.png")

    # Fuentes pixeladas\    
    fuente_titulo = pygame.font.Font(FONT_PATH, 30)
    fuente_opciones = pygame.font.Font(FONT_PATH, 18)

    opciones = ["Música: ON", "Efectos: ON", "Volver"]
    seleccion = 0
    music_on = True
    effects_on = True
    reloj = pygame.time.Clock()

    while True:
        # Dibujar fondo y título
        pantalla.blit(pygame.transform.scale(imagen_fondo, pantalla.get_size()), (0, 0))
        titulo = fuente_titulo.render("Configuración", True, COLOR_TEXTO)
        pantalla.blit(
            titulo,
            (pantalla.get_width() // 2 - titulo.get_width() // 2, 100)
        )

        # Dibujar opciones con estado dinámico
        for i, texto in enumerate(opciones):
            color = COLOR_SELECCION if i == seleccion else COLOR_TEXTO
            render = fuente_opciones.render(texto, True, color)
            pantalla.blit(
                render,
                (pantalla.get_width() // 2 - render.get_width() // 2, 220 + i * 50)
            )

        pygame.display.flip()

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    # Lógica de toggles
                    if seleccion == 0:  # Música
                        music_on = not music_on
                        opciones[0] = f"Música: {'ON' if music_on else 'OFF'}"
                        if music_on:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    elif seleccion == 1:  # Efectos
                        effects_on = not effects_on
                        opciones[1] = f"Efectos: {'ON' if effects_on else 'OFF'}"
                        if effects_on:
                            pygame.mixer.unpause()
                        else:
                            pygame.mixer.pause()
                    else:  # Volver
                        return

        reloj.tick(30)
