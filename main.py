# jetdash/main.py
import pygame
from menu import mostrar_menu

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("JetDash")

reloj = pygame.time.Clock()
ejecutando = True

mostrar_menu(pantalla)

# Loop principal
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((135, 206, 235))  # color cielo
    # Aquí se dibujarían jugador, obstáculos, fondo, etc.

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()