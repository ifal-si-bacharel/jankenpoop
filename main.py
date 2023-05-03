import pygame
from src.config.window import window
from src.config.game_params import setup_clock
from src.game_screen.screen import *

def update():
  screen(gameScreen)
  return

def draw_window():
  pygame.display.update()

def main():
  run = True
  while run:
    setup_clock()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      update()
      draw_window()

  pygame.quit()

if __name__ == '__main__':
  gameScreen = window()
  
    
  main()
  