import pygame as pg
from src.config.window import screen_width, screen_height, window
from src.common.components.text import Text

class Button():
  
  display = window()
    
  def __init__(self, coordx,coordy, color=(0,0,0), name='',img='', width = 100, height = 100, ):
    self.coordy = coordy-height/2
    self.coordx = ((screen_width() / 12) * coordx)-width/2
    self.color = color
    self.img = img
    self.name = name
    self.width = width
    self.height = height
    self.button_area = pg.Rect(self.coordx , self.coordy, self.width , self.height)


  def draw(self):
    """
    desenha botões na tela:
    """
    
    if self.name:
      pg.draw.rect(self.display, self.color, self.button_area)
      text = Text(self.name, (255, 255, 255), self.coordx, self.coordy)
      text.draw()
    if self.img:
      image = pg.image.load(self.img)
      image_on_screen = pg.transform.scale(image, (self.width,self.height))
      self.display.blit(image_on_screen, (self.coordx, self.coordy))
      
  def onclick(self, func): 
    """verifica se o botão foi clicado"""
    mousePosition = pg.mouse.get_pos()
    if self.button_area.collidepoint(mousePosition):
      if pg.mouse.get_pressed()[0] == 1:
        func()

