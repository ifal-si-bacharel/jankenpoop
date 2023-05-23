import pygame as pg
from src.config.window import screen_width, screen_height, window
from src.common.components.text import Text

class Button():
  
  display = window()
    
  def __init__(self, coordx,coordy, color, name, width = 100, height = 100, ):
    self.coordy = coordy

    self.coordx = coordx
    self.color = color
    self.name = name
    self.width = width
    self.height = height
    self.button_area = pg.Rect(screen_width() / self.coordx - 50, self.coordy, self.width , self.height)


  def draw(self):
    """
    desenha botões na tela:
    """
    pg.draw.rect(self.display, self.color, self.button_area)
    
    if self.name:
      text = Text(self.name, (255, 255, 255), self.coordx, self.coordy)
      text.draw()
      
  def onclick(self, func): 
    """verifica se o botão foi clicado"""
    mousePosition = pg.mouse.get_pos()
    if self.button_area.collidepoint(mousePosition):
      if pg.mouse.get_pressed()[0] == 1:
        func()

