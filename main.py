import pygame
from src.config.window import window
from src.config.game_params import setup_clock
from src.common.screen_display import frame
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def main():
  run = True
  
  while run:
    pygame.mixer.music.set_volume(float(config['GAMEPARAMS']['Volume']))  # Ajusta o volume da música 
    setup_clock()
    frame()
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  pygame.quit()

if __name__ == '__main__':
  window()
  main()
  