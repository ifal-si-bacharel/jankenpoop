from src.config.window import window, screen_height, screen_width
from src.common.components.button import Button
from src.common.components.text import Text
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen
import pygame
import pygame.time

display = window()
xtemplate = screen_width()
ytemplate = screen_height() / 1.5 - 50
#timer
clock = pygame.time.Clock()
time_start = pygame.time.get_ticks() 

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
check = ['','',[3,3]]


def end_round():
  global time_start, check, text, player_choice_text, machine_choice_text
  time_start = pygame.time.get_ticks() 
  player_choice_text = Text('', (255, 255, 255), 6,135)
  machine_choice_text = Text('', (255, 255, 255), 2,165)
  text = Text('', (255,255,255), 6,200)
  check = ['','',[3,3]]
  screen.switch_screen('menu')

def choice(option):
  global time_start, check, text, player_choice_text, machine_choice_text

  check = player_choice(option)

  player_choice_text = Text(check[1][0], (255, 255, 255), 6,135)
  
  machine_choice_text = Text(check[1][1], (255, 255, 255), 2,165)

  text = Text(check[0], (255,255,255), 6,200)


  if 0 in check[2]:
    end_round()


def update_screen():
  global time_decorrido_text
  time_decorrido = 60 - (pygame.time.get_ticks() - time_start) / 1000
  time_decorrido_text = Text(f'Time: {time_decorrido:.0f}s', (255, 255, 255), 2, 6)
  if time_decorrido <= 0:
    end_round()
  button_pedra.onclick(lambda:choice(1))
  button_papel.onclick(lambda:choice(2))
  button_tesoura.onclick(lambda:choice(3))
  
  

   

def draw_screen():
  text.draw()  
  player_choice_text.draw()
  time_decorrido_text.draw()
  clock.tick()
  machine_choice_text.draw()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
  x = 0 
  x2 = 40
  for i in range(1,4):
    if check[2][0]>= i:
      display.blit(full_heart, (x, 0))
    else:
      display.blit(empty_heart, (x, 0))
    x += 40
  for i in range(1,4):
    if check[2][1]>= i:
      display.blit(full_heart, (xtemplate - x2, 0))
    else:
      display.blit(empty_heart, (xtemplate -x2, 0))
    x2 += 40


