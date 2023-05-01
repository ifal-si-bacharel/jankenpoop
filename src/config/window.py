import configparser
import pygame

config = configparser.ConfigParser()
config.read('config.ini')

WIDTH = int(config['WINDOW']['Width'])
HEIGHT = int(config['WINDOW']['Height'])

def window():
  """
    Função que configura a tela do jogo
  """
  pygame.display.set_caption(config['WINDOW']['GameName'])
  return pygame.display.set_mode((WIDTH, HEIGHT))
