from src.common.components.button import Button
from src.common.components.text import Text
from src.config.window import screen_height, screen_width
import src.common.screen_display as screen
import pygame
import time

play_music = False
def update_screen(result):
    global rscreen,play_music

    

    ytemplate = screen_height()/2
    
    if result == 1:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/victory.png',width=screen_width(),height=screen_height())
        if not play_music:
          pygame.mixer.music.load("assets/music/music_victory.ogg")
          pygame.mixer_music.play()
          play_music = True 
    elif result == -1:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/defeat.png',width=screen_width(),height=screen_height())
        if not play_music:
          pygame.mixer.music.load("assets/music/music_lose.ogg")
          pygame.mixer_music.play()
          play_music = True 
    else:
        rscreen = Button(6,ytemplate,img='assets/sprites/resultscreens/timeout.png',width=screen_width(),height=screen_height())
        if not play_music:
          pygame.mixer.music.load("assets/music/music_lose.ogg")
          pygame.mixer_music.play()
          play_music = True 

    
        

def draw_screen():
    global play_music
    rscreen.draw()
    pygame.display.update()
    time.sleep(3)
    play_music = False
    pygame.mixer.music.stop()
    screen.switch_screen('menu')