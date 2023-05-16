from src.config.window import window, screen_height
from src.common.components.button import Button
from src.common.components.text import Text
from src.modules.game_screen.script.match import player_choice
import src.common.screen_display as screen


display = window()
ytemplate = screen_height() / 1.5 - 50

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

def pedra():
  choice(1)
def papel():
  choice(2)
def tesoura():
  choice(3)

def update_screen():
  button_pedra.onclick(pedra)
  button_papel.onclick(papel)
  button_tesoura.onclick(tesoura)
    
def draw_screen():
  
  text.draw()  
  player_choice_text.draw()
  machine_choice_text.draw()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
  



