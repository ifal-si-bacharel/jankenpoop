import pygame
from src.config.window import window
from src.config.game_params import setup_clock
from src.modules.game_screen.game_screen import update_screen, draw_screen

def update():
  update_screen()

def draw_window():
  draw_screen()
  pygame.display.update()

def main():
  """
    Função principal para iniciar a aplicação
  """
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
  window()
    
  main()
  