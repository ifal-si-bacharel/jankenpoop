import pygame as pg
from src.config.window import window
from src.common.components.text import Text

class Button():
  display = window()

  screen_width = display.get_width()
  screen_height = display.get_height()
    
  def __init__(self, coordx, color, name, width = 100, height = 100):
    self.coordy = self.screen_height / 1.5 - 50
    self.coordx = coordx
    self.color = color
    self.name = name
    self.width = width
    self.height = height
    
    self.buttonArea = pg.Rect(self.screen_width / self.coordx - 50, self.coordy, self.width , self.height)

  def draw(self):
    """
    desenha botões na tela:
    """
    pg.draw.rect(self.display, self.color, self.buttonArea)
    
    if self.name:
      text = Text(self.name, (255, 255, 255), self.coordx, self.coordy)
      text.draw()
      
  def onclick(self, func, param = None): 
    """verifica se o botão foi clicado"""
    mousePosition = pg.mouse.get_pos()
    if self.buttonArea.collidepoint(mousePosition):
      if pg.mouse.get_pressed()[0] == 1:
        return func(param)