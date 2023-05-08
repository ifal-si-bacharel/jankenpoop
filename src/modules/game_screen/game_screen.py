from src.config.window import window
from src.common.components.button import Button
from src.modules.game_screen.script.match import player_choice,machine_choice,exit
from src.common.components.text import Text


display = window()
display_width = display.get_width()

try:
    tela = tela
except:
    tela = 0

button_start = Button(2,(255,255,255),'start')
button_pedra = Button(5,(200,0,0),'pedra')
button_papel = Button(2,(0,200,0),'papel')
button_tesoura = Button(1.25,(0,0,200),'tesoura')

welcome_text = Text("Bem-vindo ao jogo! Faça sua escolha.", (255, 255, 198), 4.5, 100)



def ping():
  print('ping')

def set_fill():
  display.fill((0,0,0))

def start_match(x):
  print(x)
  x = 1
  print(x)

def choice(option):
  set_fill()
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

def menu_screen():
  
  welcome_text.draw()
  button_start.draw()

def match_screen():
  button_pedra.onclick(choice,1)
  button_papel.onclick(choice,2)
  button_tesoura.onclick(choice,3)
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()


def update_screen():
  set_fill()
  
  button_start.onclick(start_match,tela)
  

def draw_screen():
  if tela:
    match_screen()
    return
  menu_screen()



