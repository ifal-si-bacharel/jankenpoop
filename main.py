import pygame
from src.config.window import window
from src.config.game_params import setup_clock

def update():
  """
    Funções para logica do jogo devem vim aqui
  """
  return

def draw_window():
  """
    Funções de renderização devem vim aqui
  """
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
  