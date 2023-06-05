import pygame as pg
from src.config.window import screen_width, screen_height, window
from src.common.components.text import Text
from src.common.components.animation import Animation

class Character():
  display = window()
  
  def __init__(self, coordx, coordy, color=(255,255,255), name='', img='',animations={}, width = 100, height = 100):
   
    self.coordy = ((screen_height() / 12) * coordy)-height/2
    self.coordx = ((screen_width() / 12) * coordx)-width/2
    self.align = coordx
    self.lifes = 3
    self.current_lifes = 3
    self.color=color
    self.img = img
    self.name = name
    self.width = width
    self.height = height
    self.animations_dir = animations
    self.animations = self.load_animations(self.animations_dir)
    self.current_animation = 'main'

  def load_animations(self, dictionary):
    list_animations = {}
    for name, dir in dictionary.items(): 
      list_animations[name] = Animation(dir=dir[0],
                                        coordx=self.coordx,
                                        coordy=self.coordy,
                                        height=self.height,
                                        width=self.width,
                                        name=name,
                                        repeat=dir[1],
                                  )
                                                                   
    return list_animations

  def takedDamage(self, damage = 1):
    self.current_lifes = self.current_lifes - damage
  
  def animate(self,lifes=True, next_animation='', current=''):
    if lifes:
      self.draw_info()
    if current:
      self.current_animation = current
    animation = self.animations[self.current_animation].play()

    if animation == 'over':
      self.current_animation = 'main'
      return self.current_animation
    self.current_animation = animation
    return self.current_animation

  def draw(self, lifes = True):  
    if self.img:
      image = pg.image.load(self.img)
      image_on_screen = pg.transform.scale(image, (self.width, self.height))
      self.display.blit(image_on_screen, (self.coordx, self.coordy))
    self.draw_info(lifes)

  def draw_info(self, lifes = True):  
    name_display = Text(self.name,self.color,self.align,coordy=self.coordy+self.height/1.5)
    name_display.draw()
    if lifes:
      full_heart = pg.image.load('assets/sprites/full_heart.png')
      empty_heart = pg.image.load('assets/sprites/empty_heart.png')
      x = self.coordx + 40
      y = self.coordy - 20
      for i in range(1,4):
        if self.current_lifes >= i:
          self.display.blit(full_heart, (x, y))
        else:
          self.display.blit(empty_heart, (x, y))
        x += 40


