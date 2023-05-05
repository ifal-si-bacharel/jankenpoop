import pygame as pg
from src.config.window import window

class Text():
  display = window()

  screen_width = display.get_width()
    
  def __init__(self, text, color, coordx, coordy):
    pg.init()

    self.font = pg.font.SysFont('Calibri', 25)
    self.coordx = coordx
    self.coordy = coordy

    self.half_font_width = self.font.get_linesize() / 2  
    self.half_font_height = self.font.get_height() / 2  
    self.CENTER_CONSTANT = 25

    self.position = (
      (self.screen_width / self.coordx - self.CENTER_CONSTANT) - self.half_font_width,
      (self.coordy + self.CENTER_CONSTANT)
    )
    
    self.text = text
    self.color = color

  def draw(self):
    self.display.blit(self.font.render(self.text, True, self.color), self.position) 