from src.config.window import window, screen_height, screen_width
from src.common.components.button import Button
from src.common.components.text import Text
from src.common.components.character import Character
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen
import pygame
import pygame.time
import time
import configparser

pygame.mixer.init()

config = configparser.ConfigParser()
config.read('config.ini')
timer_limit = int(config['GAMEPARAMS']['Timer'])
display = window()
xtemplate = screen_width()
ytemplate = (screen_height()/12) * 10
ytext = (screen_height()/12) * 9




#background
yhalf = (screen_height()/12) * 5

rscreen = Button(6,yhalf,img='assets/sprites/background/background.jpg',width=screen_width(),height=screen_height())
rground = Button(6,ytemplate,img='assets/sprites/background/chao.png',width=screen_width(),height=255)
#timer
clock = pygame.time.Clock()

#buttons
button_pedra = Button(3,ytemplate,img='assets/sprites/buttons/rock.png')
button_papel = Button(6,ytemplate,img='assets/sprites/buttons/paper.png')
button_tesoura = Button(9,ytemplate,img='assets/sprites/buttons/siccssors.png')
pause = Button(1,40,img='assets/sprites/buttons/pause.png',width=50,height=50)

#set_outputs
text = Text('', (255,255,255), 6,ytext)
check = ['','']

#set_music
musicmatch_played = False  # para controlar a reprodução da música

def set_character_state(state):
  global character_state
  character_state = state

def get_character_state():
  global character_state
  return character_state 

def create_characters():
  global player_character, enemy_character
  set_character_state('main')
  player_character = Character(3,
                             7,
                             animations={'main':['assets/sprites/player/main',2],
                                          'wait':['assets/sprites/player/wait',3]},
                             width=200,
                             height=200,
                             name='VOCÊ',
                             color=(0,194,254))
  enemy_character = Character(9,
                              7,
                              animations={'blink':['assets/sprites/enemy/blink',0],
                                          'main':['assets/sprites/enemy/main',2],
                                          'wait':['assets/sprites/enemy/wait',3]},
                              width=200,
                              height=200,
                              name='INIMIGO',
                              color=(255,0,0))

#characters
create_characters()


def play_music():
  global musicmatch_played
  if not musicmatch_played:
        pygame.mixer.music.load("assets/music/musicmatch.ogg")
        pygame.mixer.music.play()
        musicmatch_played = True
  

def choice(option):
  global time_start, check, text
  
  set_character_state('wait')

  check = player_choice(option)
  text = Text(check[0], (255,255,255), 6,ytext)

  if check[0] == "Você ganhou!":
    enemy_character.current_lifes -= 1      
  elif check[0] == "Você perdeu!":
    player_character.current_lifes -= 1  

def countdown_tick(time_elapsed):
  global time_decorrido_text, time_decorrido
  time_decorrido = timer_limit - time_elapsed / 1000
  time_decorrido_text = Text(f'{time_decorrido:2.0f}', (255,255,255), 6,25,60)
  if time_decorrido <= 0:
    end_round(0,0)

def end_round(result, type=0):
  global time_start, check, text, musicmatch_played,player_character,enemy_character
  time_start = pygame.time.get_ticks() 
  musicmatch_played = False
  pygame.mixer.music.stop()
  create_characters()

  text = Text('', (255,255,255), 6,ytext)
  if result == 0:
    if type == 0:
      screen.switch_screen('timeout')
    else:
      screen.switch_screen('gameover')
  else:
    screen.switch_screen('win')

def draw_result():
  player_character.img = f'assets/sprites/player/{check[1][0]}'
  enemy_character.img = f'assets/sprites/enemy/{check[1][1]}'
  player_character.draw(True)
  enemy_character.draw(True)
  text.draw()
  pygame.display.update()
  time.sleep(2)
  set_character_state('main')
    

#screen_funcs
def update_screen(time_start):
    play_music()
    countdown_tick(time_start)
    button_pedra.onclick(lambda: choice(1))
    button_papel.onclick(lambda: choice(2))
    button_tesoura.onclick(lambda: choice(3))
    pause.onclick(lambda: screen.switch_screen('pause'))
    
def draw_screen():
  if time_decorrido <= timer_limit-1:
    rscreen.draw()
    rground.draw()
    if get_character_state() == 'main':
      current_player_animation = player_character.animate()
      enemy_character.animate()
      if time_decorrido <= 30:
        time_decorrido_text.draw()
      button_pedra.draw()
      button_papel.draw()
      button_tesoura.draw()
      pause.draw()
    elif get_character_state() == 'wait':
      current_player_animation = player_character.animate(current=get_character_state(),lifes =False)
      enemy_character.animate(current=get_character_state(),lifes = False)
      if current_player_animation == 'main':
        set_character_state('play')
    elif character_state ==  'play':
      draw_result()
      if player_character.current_lifes <= 0:
        end_round(0,1)
      if enemy_character.current_lifes <= 0:
        end_round(1)

    return
  return


