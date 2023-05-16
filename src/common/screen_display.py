from src.config.window import window
import src.modules.game_screen.game_screen as match
import src.modules.menu_screen.menu_screen as menu


current_screen = 'menu'
display = window()

def switch_screen(screen):
  print(screen)
  global current_screen 
  current_screen = screen
  
  

def frame():
  if current_screen == 'menu':
    display.fill((0,0,0))
    menu.update_screen()
    menu.draw_screen()
  if current_screen == 'match':
    display.fill((0,0,0))
    match.update_screen()
    match.draw_screen()
