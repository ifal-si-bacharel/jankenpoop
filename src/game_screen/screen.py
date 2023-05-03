import pygame as pg
from src.config.window import window
from src.game_screen.components.button import Button
from src.game_screen.script.match import player_choice

display = window()
width = display.get_width()
height = display.get_height()

def set_fill():
    display.fill((60,68,79)) 
def draw_screen():
    set_fill()
    button_pedra.draw()
    button_papel.draw()
    button_tesoura.draw()
    
def update_screen():
    if button_pedra.is_hover():
        player_choice(1)
        return
    
    # if
    # button_papel.is_hover()
    # button_tesoura.is_hover()  
    
button_pedra = Button(5,(255,0,0),'pedra',width,height)
button_papel = Button(2,(0,255,0),'papel',width,height)
button_tesoura = Button(1.25,(0,0,255),'tesoura',width,height)

    
