from src.config.window import window, screen_height, screen_width
from src.common.components.button import Button
from src.common.components.text import Text
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen
import pygame
import sys
import pygame.time

display = window()
xtemplate = screen_width()
ytemplate = screen_height() / 1.5 - 50

#hearts
full_heart = pygame.image.load('src/sprites/full_heart.png')
empty_heart = pygame.image.load('src/sprites/empty_heart.png')

full_heart_on_screen = pygame.transform.scale(full_heart, (20, 20))
empty_heart_on_screen = pygame.transform.scale(empty_heart, (20, 20))

button_pedra = Button(5,ytemplate,(200,0,0),'pedra')
button_papel = Button(2,ytemplate,(0,200,0),'papel')
button_tesoura = Button(1.25,ytemplate,(0,0,200),'tesoura')
text = Text('', (255,255,255), 6,200)
player_choice_text = Text('', (255, 255, 255), 6,135)
machine_choice_text = Text('', (255, 255, 255), 2,165)

def choice(option):
  global text, player_choice_text, machine_choice_text

  check = player_choice(option)

  player_choice_text = Text(check[1][0], (255, 255, 255), 6,135)
  
  machine_choice_text = Text(check[1][1], (255, 255, 255), 2,165)

  text = Text(check[0], (255,255,255), 6,200)


  if 0 in check[2]:
    player_choice_text = Text('', (255, 255, 255), 6,135)
    machine_choice_text = Text('', (255, 255, 255), 2,165)
    text = Text('', (255,255,255), 6,200)
    screen.switch_screen('menu')

  
def update_screen():
  button_pedra.onclick(lambda:choice(1))
  button_papel.onclick(lambda:choice(2))
  button_tesoura.onclick(lambda:choice(3))

clock = pygame.time.Clock()
time_start = pygame.time.get_ticks()    

def draw_screen():
  text.draw()  
  player_choice_text.draw()
  time_decorrido = (pygame.time.get_ticks() - time_start) / 1000
  time_decorrido_text = Text(f'Time: {time_decorrido:.1f}s', (255, 255, 255), 2, 6)
  time_decorrido_text.draw()
  clock.tick()
  machine_choice_text.draw()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
  display.blit(full_heart, (0,0))
  display.blit(full_heart, (40,0))
  display.blit(full_heart, (80,0))
  display.blit(full_heart, (xtemplate - 40, 0))
  display.blit(full_heart, (xtemplate - 80,0))
  display.blit(full_heart, (xtemplate - 120,0))


