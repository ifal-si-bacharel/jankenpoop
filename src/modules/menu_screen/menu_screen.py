import pygame
import src.common.screen_display as screen
from src.common.components.text import Text

welcome_text = Text("Bem-vindo ao jogo Jankenpoop!", (255, 255, 198), 6, 190)
press_start = Text("Pressione Enter para iniciar", (255, 255, 198), 6, 220)

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
    welcome_text.draw()
    press_start.draw()
