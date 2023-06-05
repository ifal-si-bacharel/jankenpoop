import pygame
from src.config.window import screen_height, screen_width
import src.common.screen_display as screen
from src.common.components.animation import Animation


bgscreen = Animation(name='background-menu',
                     dir='assets/sprites/background/menu_background',
                     coordx=0,
                     coordy=0,
                     height=screen_height(),
                     width=screen_width(),
                     loop=True,
                     type_image='jpg',
                     repeat=0)

play_music = False
def update_screen():
  global play_music
  keys = pygame.key.get_pressed()
  if not play_music:
    pygame.mixer.music.load("assets/music/musicmenu.ogg")
    pygame.mixer_music.play()
    play_music = True 

  if keys[pygame.K_SPACE]:
    play_music = False
    pygame.mixer.music.stop()
    screen.switch_screen('match')

def draw_screen():
    bgscreen.play()
