from src.config.window import window
import src.modules.game_screen.game_screen as match
import src.modules.menu_screen.menu_screen as menu

print('ping')
telas = [menu,match]
tela_atual= telas[1]
display = window()
screen_width = display.get_width()
screen_height = display.get_height()

def set_fill():
  display.fill((0,0,0))

def frame():
    tela_atual.update_screen()
    tela_atual.draw_screen()