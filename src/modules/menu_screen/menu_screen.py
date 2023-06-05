import pygame
from src.config.window import screen_height, screen_width
import src.common.screen_display as screen
from src.common.components.button import Button

ytemplate = screen_height()/2
bgscreen = Button(6,ytemplate,img='assets/sprites/MenuAnimado.gif',width=screen_width(),height=screen_height())

play_music = False
def update_screen():
  global play_music
  keys = pygame.key.get_pressed()
  if not play_music:
    pygame.mixer.music.load("assets/music/musicmenu.ogg")
    pygame.mixer_music.play()
    play_music = True 

  if keys[pygame.K_RETURN]:
    play_music = False
    pygame.mixer.music.stop()
    screen.switch_screen('match')

def draw_screen():
    bgscreen.draw()
