from src.config.window import window
import src.modules.game_screen.game_screen as match
import src.modules.menu_screen.menu_screen as menu
import src.modules.result_screen.result_screen as result
import src.modules.pause_screen.pause as pause
import pygame

current_screen = 'menu'
display = window()
timer_stack = 0
last_mark = 0

def switch_screen(screen):
  global current_screen, last_mark, timer_stack
  current_screen = screen
  if screen == 'pause':
    timer_stack += clock_tick()
  if screen == 'match':
    last_mark = pygame.time.get_ticks()
  if screen == 'result':
    timer_stack = 0
  
  
  
def clock_tick():
  global time
  return pygame.time.get_ticks() - last_mark 

def frame():
  if current_screen == 'menu':
    display.fill((0,0,0))
    menu.update_screen()
    menu.draw_screen()
  if current_screen == 'match':
    match.update_screen(clock_tick()+timer_stack)
    display.fill((0,0,0))
    match.draw_screen()
  if current_screen == 'win':
    display.fill((0,0,0))
    result.update_screen(1)
    result.draw_screen()
  if current_screen == 'timeout':
    display.fill((0,0,0))
    result.update_screen(0)
    result.draw_screen()
  if current_screen == 'gameover':
    display.fill((0,0,0))
    result.update_screen(-1)
    result.draw_screen()
  if current_screen == 'pause':
    display.fill((0,0,255,))
    pause.update_screen()
    pause.draw_screen()
