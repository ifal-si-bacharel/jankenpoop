import pygame
from src.config.window import screen_height, screen_width
import src.common.screen_display as screen
from src.common.components.button import Button


ytemplate = screen_height()/2
bgscreen = Button(6,ytemplate,img='assets/sprites/background/pause.jpg',width=screen_width(),height=screen_height())


def update_screen():
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_SPACE]:
        screen.switch_screen('match')

def draw_screen():
    bgscreen.draw()
