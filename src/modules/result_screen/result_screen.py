from src.common.components.button import Button
from src.common.components.text import Text
from src.config.window import screen_height, screen_width
import src.common.screen_display as screen
import pygame
import time
def update_screen(result):
    global rscreen,return_text
    ytemplate = screen_height()/2
    
    if result == 1:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/victory.png',width=screen_width(),height=screen_height())
        
    elif result == -1:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/defeat.png',width=screen_width(),height=screen_height())
        
    else:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/timeout.png',width=screen_width(),height=screen_height())
       

    
        

def draw_screen():
    rscreen.draw()
    pygame.display.update()
    time.sleep(4)
    screen.switch_screen('menu')