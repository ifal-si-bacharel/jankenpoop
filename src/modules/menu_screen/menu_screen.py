import src.common.screen_display as screen
from src.common.components.text import Text
from src.common.components.button import Button

welcome_text = Text("Bem-vindo ao jogo! Faça sua escolha.", (255, 255, 198), 4.5, 100)
button = Button(2,200,(255,255,255),'start')
def update_screen():
    button.onclick(lambda: screen.switch_screen('match'))

def draw_screen():
    button.draw()

