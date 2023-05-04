import pygame as pg
from src.config.window import window

class Button():
  display = window()

  width = display.get_width()
  height = display.get_height()
    
  def __init__(self, coordx, color, name):
    self.coordy = self.height / 1.5-50
    self.coordx = coordx
    self.position = (self.coordx,self.coordy)
    self.color = color
    self.name = name
    self.buttonArea = pg.Rect(self.width / self.coordx-50, self.coordy,100,100)

  def draw(self):
    """
    desenha botões na tela:
    """
    pg.draw.rect(self.display,self.color,self.buttonArea)

  def is_hover(self):
    """verifica se o botão foi clicado"""
    mousePosition = pg.mouse.get_pos()
    if self.buttonArea.collidepoint(mousePosition):
      if pg.mouse.get_pressed()[0] == 1:
        return self.name