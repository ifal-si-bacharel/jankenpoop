import pygame as pg
from src.config.window import window, screen_width

class Text():

  display = window()
    
  def __init__(self, text, color, coordx, coordy):
    pg.init()

    self.font = pg.font.SysFont('Calibri', 25)
    self.coordx = coordx
    self.coordy = coordy
    self.text = text
    self.half_font_width = len(self.text)*11  
    self.half_font_height = self.font.get_height() / 2  
    self.CENTER_CONSTANT = 25

    self.position = (
      ((screen_width() /12) * self.coordx) - self.half_font_width/2,
      (self.coordy + self.CENTER_CONSTANT+self.half_font_height)
    )
    
    
    self.color = color

  def draw(self):
    self.display.blit(self.font.render(self.text, True, self.color), self.position) 
