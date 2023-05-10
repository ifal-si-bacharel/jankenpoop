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


def choice(option):
  
  display.fill((0,0,0))
  check = player_choice(option)
  player_choice_text = Text(check[1], (255, 255, 255), 6,135)
  
  machine_choice_text = Text(check[2], (255, 255, 255), 2,165)

  player_choice_text.draw()
  machine_choice_text.draw()
  if check[0] == 1:
    text = Text("Você ganhou!", (0,255,0), 6,200)
    text.draw()
  elif check[0] == 0:
    text = Text("Empate!", (0,0,255), 6,200)
    text.draw()
  else:
    text = Text("Você perdeu!", (255,0,0), 6,200)
    text.draw()  

  if check[3] == 0 or check[4] == 0:
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
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
  



