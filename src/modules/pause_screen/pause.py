import pygame
import src.common.screen_display as screen
from src.common.components.text import Text

welcome_text = Text("JOGO PAUSADO", (255, 255, 198), 6, 190)
press_start = Text("Pressione Enter para retomar", (255, 255, 198), 6, 220)

def update_screen():
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_RETURN]:
        screen.switch_screen('match')

def draw_screen():
    welcome_text.draw()
    press_start.draw()