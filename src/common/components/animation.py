import pygame as pg
from src.config.window import window
import os

class Animation():
  def __init__(self,dir,coordx,coordy,repeat,name,loop=False,width = 100,height = 100,type_image='png'):
    self.type_image = type_image
    self.display = window()
    self.coordy = coordy
    self.coordx = coordx
    self.align = coordx
    self.width = width
    self.height = height
    self.name = name
    self.dir = dir
    self.frame = 0
    self.repeat = repeat 
    self.loop = loop
    self.current_repeat = 0
    self.total_frames = self.set_total_frames()

  def set_total_frames(self): 
    stack = 0 
    for path in os.listdir(self.dir):
      if os.path.isfile(os.path.join(self.dir, path)):
          stack += 1

    return stack

  def play(self,next_animation= ''):
    animation = pg.image.load(f'{self.dir}/{self.frame}.{self.type_image}')
    animation_on_screen = pg.transform.scale(animation, (self.width, self.height))
    self.display.blit(animation_on_screen, (self.coordx, self.coordy))
    
    if self.frame == self.total_frames-1:
      if self.loop:
        self.frame = 0
        return self.name
      elif self.repeat:
        if self.current_repeat == self.repeat:
          self.current_repeat = 0
          self.frame = 0
          return next_animation if next_animation else 'over'
        self.frame = 0
        self.current_repeat += 1
        return self.name
      elif next_animation:
        self.frame = 0
        return next_animation
      return self.name
    else:
      self.frame += 1
      return self.name
    