import configparser
import pygame

config = configparser.ConfigParser()
config.read('config.ini')

clock = pygame.time.Clock()

def setup_clock():
  """
    Função de configura a taxa de atualização do jogo
  """

  clock.tick(int(config['GAMEPARAMS']['Fps']))
