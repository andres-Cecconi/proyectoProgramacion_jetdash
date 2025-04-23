# jetdash/recursos.py
import pygame
import os

ASSETS_DIR = os.path.join("assets")
IMG_DIR = os.path.join(ASSETS_DIR, "img")
SND_DIR = os.path.join(ASSETS_DIR, "sounds")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")

def cargar_imagen(nombre):
    ruta = os.path.join(IMG_DIR, nombre)
    return pygame.image.load(ruta).convert_alpha()

def cargar_sonido(nombre):
    ruta = os.path.join(SND_DIR, nombre)
    return pygame.mixer.Sound(ruta)

def cargar_musica(nombre):
    ruta = os.path.join(MUSIC_DIR, nombre)
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

# Recursos a cargar globalmente
def cargar_todos_los_recursos():
    recursos = {
        "jugador": cargar_imagen("jugador.png"),
        "obstaculo": cargar_imagen("misil.png"),
        "fondo_1": cargar_imagen("fondo1.png"),
        "fondo_2": cargar_imagen("fondo2.png"),
        "colision": cargar_sonido("colision.wav"),
        "jetpack": cargar_sonido("jetpack.wav"),
        "punto": cargar_sonido("punto.wav"),
    }
    return recursos
