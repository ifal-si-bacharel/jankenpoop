import src.common.screen_display as switch_screen
from src.common.components.text import Text
from src.common.components.button import Button

welcome_text = Text("Bem-vindo ao jogo! Faça sua escolha.", (255, 255, 198), 4.5, 100)
def update_screen():
    print('hi')

def draw_screen():
    button = Button(2,(255,255,255),'start')
    button.onclick(lambda: switch_screen('match'))
    button.draw()

