import pygame as pg
from src.config.window import screen_width, screen_height, window
from src.common.components.text import Text

class Character():
  
  display = window()
    
  def __init__(self, coordx,coordy,color=(255,255,255), name='',img='', width = 100, height = 100, ):
    self.coordy = ((screen_height() / 12) * coordy)-height/2
    self.coordx = ((screen_width() / 12) * coordx)-width/2
    self.align = coordx
    self.lifes = 3
    self.current_lifes = 3
    self.img = img
    self.color = color
    self.name = name
    self.width = width
    self.height = height
    


  def draw(self,lifes = True):
    if self.img:
      image = pg.image.load(self.img)
      image_on_screen = pg.transform.scale(image, (self.width, self.height))
      self.display.blit(image_on_screen, (self.coordx, self.coordy))

    name_display = Text(self.name,self.color,self.align,coordy=self.coordy+self.height/1.5)

    name_display.draw()
    if lifes:
      full_heart = pg.image.load('src/sprites/full_heart.png')
      empty_heart = pg.image.load('src/sprites/empty_heart.png')
      x = self.coordx + 40
      y = self.coordy - 20
      for i in range(1,4):
        if self.current_lifes >= i:
          self.display.blit(full_heart, (x, y))
        else:
          self.display.blit(empty_heart, (x, y))
        x += 40