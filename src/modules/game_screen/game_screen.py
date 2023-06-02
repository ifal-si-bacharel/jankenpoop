from src.config.window import window, screen_height, screen_width
from src.common.components.button import Button
from src.common.components.text import Text
from src.common.components.character import Character
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen
import pygame
import pygame.time
import time
pygame.mixer.init()


display = window()
xtemplate = screen_width()
ytemplate = (screen_height()/12) * 10

#timer
clock = pygame.time.Clock()

#character
player_character = Character(3,
                             5,
                             img='src/sprites/player/main.png',
                             width=200,
                             height=200,
                             name='VOCÊ',
                             color=(0,0,255))
enemy_character = Character(9,
                            5,
                            img='src/sprites/enemy/main.png',
                            width=200,
                            height=200,
                            name='INIMIGO',
                            color=(255,0,0))

#hearts
full_heart = pygame.image.load('src/sprites/full_heart.png')
empty_heart = pygame.image.load('src/sprites/empty_heart.png')
full_heart_on_screen = pygame.transform.scale(full_heart, (20, 20))
empty_heart_on_screen = pygame.transform.scale(empty_heart, (20, 20))

#buttons
button_pedra = Button(3,ytemplate,img='src/sprites/buttons/rock.png')
button_papel = Button(6,ytemplate,img='src/sprites/buttons/paper.png')
button_tesoura = Button(9,ytemplate,img='src/sprites/buttons/siccssors.png')
pause = Button(1,40,img='src/sprites/buttons/pause.png',width=50,height=50)

#set_outputs
text = Text('', (255,255,255), 6,300)
player_choice_text = Text('', (255, 255, 255), 6,135)
machine_choice_text = Text('', (255, 255, 255), 2,165)
check = ['','',[3,3]]

#set_music
musicmatch_played = False  # para controlar a reprodução da música

def play_music():
  global musicmatch_played
  if not musicmatch_played:
        pygame.mixer.music.load("src/music/musicmatch.ogg")
        pygame.mixer.music.play()
        musicmatch_played = True
  

def choice(option):
  global time_start, check, text, player_choice_text, machine_choice_text
  
  check = player_choice(option)
  text = Text(check[0], (255,255,255), 6,300)

  if check[0] == "Você ganhou!":
    enemy_character.current_lifes -= 1      
  elif check[0] == "Você perdeu!":
    player_character.current_lifes -= 1  
  
  display.fill((0,0,0))
  player_character.img = f'src/sprites/player/wait.png'
  enemy_character.img = f'src/sprites/enemy/wait.png'
  player_character.draw(False)
  enemy_character.draw(False)
  pygame.display.update()
  time.sleep(3)
  
  display.fill((0,0,0))
  player_character.img = f'src/sprites/player/{check[1][0]}'
  enemy_character.img = f'src/sprites/enemy/{check[1][1]}'
  player_character.draw(False)
  enemy_character.draw(False)
  text.draw()
  pygame.display.update()
  time.sleep(2)

  player_character.img = f'src/sprites/player/main.png'
  enemy_character.img = f'src/sprites/enemy/main.png'

  if player_character.current_lifes == 0:
    end_round(0,1)
  if enemy_character.current_lifes == 0:
    end_round(1)

def countdown_tick(time_elapsed):
  global time_decorrido_text, time_decorrido
  time_decorrido = 120 - time_elapsed / 1000
  time_decorrido_text = Text(f'{time_decorrido:2.0f}', (255, 255, 255), 6,3)
  if time_decorrido <= 0:
    end_round(0,0)

def end_round(result, type=0):
  global time_start, check, text, player_choice_text, machine_choice_text, musicmatch_played,player_character,enemy_character
  time_start = pygame.time.get_ticks() 
  musicmatch_played = False
  print(musicmatch_played)
  pygame.mixer.music.stop()
  player_character = Character(3,
                             5,
                             img='src/sprites/player/main.png',
                             width=200,
                             height=200,
                             name='VOCÊ',
                             color=(0,0,255))
  enemy_character = Character(9,
                            5,
                            img='src/sprites/enemy/main.png',
                            width=200,
                            height=200,
                            name='INIMIGO',
                            color=(255,0,0))

  text = Text('', (255,255,255), 6,200)
  if result == 0:
    if type == 0:
      screen.switch_screen('timeout')
    else:
      screen.switch_screen('gameover')
  else:
    screen.switch_screen('win')


#screen_funcs
def update_screen(time_start):
    play_music()
    countdown_tick(time_start)
    button_pedra.onclick(lambda: choice(1))
    button_papel.onclick(lambda: choice(2))
    button_tesoura.onclick(lambda: choice(3))
    pause.onclick(lambda: screen.switch_screen('pause'))
    
  
def draw_screen():
  if time_decorrido <=30:
    time_decorrido_text.draw()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
  player_character.draw()
  enemy_character.draw()
  pause.draw()



