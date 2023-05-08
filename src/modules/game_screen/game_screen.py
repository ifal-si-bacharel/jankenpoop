from src.common.screen_display import *
from src.common.components.button import Button
from src.common.components.text import Text
from src.modules.game_screen.script.match import player_choice

button_start = Button(2,(255,255,255),'start')
button_pedra = Button(5,(200,0,0),'pedra')
button_papel = Button(2,(0,200,0),'papel')
button_tesoura = Button(1.25,(0,0,200),'tesoura')

def choice(option):
  screen.set_fill()
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


def update_screen():
  button_pedra.onclick(choice,1)
  button_papel.onclick(choice,2)
  button_tesoura.onclick(choice,3)
    
def draw_screen():
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()



