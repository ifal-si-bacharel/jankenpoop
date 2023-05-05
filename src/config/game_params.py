import configparser
import pygame

config = configparser.ConfigParser()
config.read('config.ini')

clock = pygame.time.Clock()

def setup_clock():
  clock.tick(int(config['GAMEPARAMS']['Fps']))
