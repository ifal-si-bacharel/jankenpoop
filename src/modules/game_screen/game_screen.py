from src.config.window import window
from src.common.components.button import Button
from src.modules.game_screen.script.match import player_choice, machine_choice, exit
from src.common.components.text import Text

display = window()

button_pedra = Button(5,(200,0,0),'pedra')
button_papel = Button(2,(0,200,0),'papel')
button_tesoura = Button(1.25,(0,0,200),'tesoura')


def set_fill():
  display.fill((0, 0, 0))

welcome_text = Text("Bem-vindo ao jogo! Faça sua escolha.", (255, 255, 198), 4.5, 100)

def choice(option):

  check = player_choice(option)
  print(check)
  player_choice_text = Text(f'Você escolheu {exit[option-1]}', (255, 255, 255), 6,135)
  machine_choice_text = Text(f'A maquina escolheu {exit[machine_choice()-1]}', (255, 255, 255), 6,165)
 
  set_fill()
  player_choice_text.draw()
  machine_choice_text.draw()
  if check == 1:
    text = Text("Você ganhou!", (255,255,255), 2, 200)
    text.draw()
  elif check == 0:
    text = Text("Empate!", (255,255,255), 2, 200)
    text.draw()
  else:
    text = Text("Você perdeu!", (255,255,255), 2, 200)
    text.draw()  
    

def update_screen():
  if button_pedra.is_hover():
    choice(1)
    
  elif button_papel.is_hover():
    choice(2)
    
  elif button_tesoura.is_hover():
    choice(3)
    


def draw_screen():
  #set_fill()
  welcome_text.draw()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
