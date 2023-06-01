from src.common.components.text import Text
import src.common.screen_display as screen
import pygame
def update_screen(result):
    global menssage, menssage_return
    menssage_return = Text("pressione Enter para voltar ao menu principal", (255, 255, 255), 5, 240)
    if result == 1:
        menssage = Text("VOCÊ VENCEU!!!", (0, 255, 0), 2.5, 200)
    elif result == -1:
        menssage = Text("VOCÊ PERDEU!!!", (255, 0, 0), 2.5, 200)
    else:
        menssage = Text("ACABOU O TEMPO!!! XD", (0, 255, 255), 2.5, 200)

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RETURN]:
        screen.switch_screen('menu')

def draw_screen():
    menssage.draw()
    menssage_return.draw()