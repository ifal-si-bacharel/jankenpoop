from src.config.window import window
from src.common.components.button import Button
from src.modules.game_screen.script.match import player_choice

display = window()

button_pedra = Button(5,(255,0,0),'pedra')
button_papel = Button(2,(0,255,0),'papel')
button_tesoura = Button(1.25,(0,0,255),'tesoura')

def set_fill():
  display.fill((60,68,79)) 

def update_screen():
  if button_pedra.is_hover():
    player_choice(1)
    
  elif button_papel.is_hover():
    player_choice(2)
    
  elif button_tesoura.is_hover():
    player_choice(3)
    

def draw_screen():
  set_fill()
  button_pedra.draw()
  button_papel.draw()
  button_tesoura.draw()
    
    # if
    # button_papel.is_hover()
    # button_tesoura.is_hover()  
    

    
