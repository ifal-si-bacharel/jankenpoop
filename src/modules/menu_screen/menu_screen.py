import pygame
import src.common.screen_display as screen
from src.common.components.text import Text
from src.common.components.button import Button

welcome_text = Text("Bem-vindo ao jogo Jankenpoop!", (255, 255, 198), 3.5, 190)
press_start = Text("Pressione START para iniciar", (255, 255, 198), 3.0, 220)


def update_screen():
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RETURN]:

        screen.switch_screen('match')


def draw_screen():
    welcome_text.draw()
    press_start.draw()

