from src.config.window import window, screen_height, screen_width
from src.common.components.button import Button
from src.common.components.text import Text
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen
import pygame
import pygame.time

pygame.mixer.init()


display = window()
xtemplate = screen_width()
ytemplate = screen_height() / 1.5 - 50
#timer
clock = pygame.time.Clock()

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

musicmatch_played = False  # para controlar a reprodução da música
pygame.mixer.music.load("src/music/musicmenu.ogg")

def end_round(result):
  global time_start, check, text, player_choice_text, machine_choice_text
  time_start = pygame.time.get_ticks() 
  player_choice_text = Text('', (255, 255, 255), 6,135)
  machine_choice_text = Text('', (255, 255, 255), 2,165)
  text = Text('', (255,255,255), 6,200)
  check = ['','',[3,3]]
  if result == 0:
    screen.switch_screen('lose')
  else:
    screen.switch_screen('win')
  

def choice(option):
  global time_start, check, text, player_choice_text, machine_choice_text

  check = player_choice(option)

  player_choice_text = Text(check[1][0], (255, 255, 255), 6,135)
  
  machine_choice_text = Text(check[1][1], (255, 255, 255), 2,165)

  text = Text(check[0], (255,255,255), 6,200)


  if check[2][0] == 0:
    end_round(0)
  if check[2][1] == 0:
    end_round(1)

def countdown_tick(time_start):
  global time_decorrido_text
  time_decorrido = 60 - (pygame.time.get_ticks() - time_start) / 1000
  time_decorrido_text = Text(f'Time: {time_decorrido:.0f}s', (255, 255, 255), 2, 6)
  if time_decorrido <= 0:
    end_round(0)

def update_screen(time_start):
    global musicmatch_played
    countdown_tick(time_start)
    if not musicmatch_played:
        pygame.mixer.music.load("src/music/musicmatch.ogg")
        pygame.mixer.music.play()
        musicmatch_played = True
    button_pedra.onclick(lambda: choice(1))
    button_papel.onclick(lambda: choice(2))
    button_tesoura.onclick(lambda: choice(3))
  
  

   

def draw_screen():
  text.draw()  
  player_choice_text.draw()
  time_decorrido_text.draw()
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


