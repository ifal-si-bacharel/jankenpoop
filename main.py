import pygame
from src.config.window import window
from src.config.game_params import setup_clock
from src.common.screen_display import frame, tela_atual

  

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
      frame()
      pygame.display.update()

  pygame.quit()

if __name__ == '__main__':
  window()
    
  main()
  