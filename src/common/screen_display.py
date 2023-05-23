from src.config.window import window
import src.modules.game_screen.game_screen as match
import src.modules.menu_screen.menu_screen as menu
import pygame

current_screen = 'menu'
display = window()

def switch_screen(screen):
  global time_start
  print(screen)
  global current_screen 
  current_screen = screen
  time_start = pygame.time.get_ticks() 
  
  

def frame():
  
  if current_screen == 'menu':
    display.fill((0,0,0))
    menu.update_screen()
    menu.draw_screen()
  if current_screen == 'match':
    display.fill((0,0,0))
    match.update_screen(time_start)
    match.draw_screen()
