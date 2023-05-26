import pygame
import src.common.screen_display as screen
from src.common.components.text import Text
from src.common.components.button import Button



welcome_text = Text("Bem-vindo ao jogo Jankenpoop!", (255, 255, 198), 3.5, 190)
press_start = Text("Pressione START para iniciar", (255, 255, 198), 3.0, 220)

pygame.mixer.music.load("music/musicmenu.ogg")
pygame.mixer_music.play()


def update_screen():
    global play_music
    play_music = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RETURN]:
        pygame.mixer.music.stop()
        screen.switch_screen('match')

def draw_screen():
    welcome_text.draw()
    press_start.draw()
