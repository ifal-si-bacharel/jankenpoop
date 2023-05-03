import configparser
import pygame as pg

config = configparser.ConfigParser()
config.read('config.ini')

width = int(config['WINDOW']['Width'])
height = int(config['WINDOW']['Height'])
def set_fill(display):
       display.fill((60,68,79)) 
def screen(display):
    set_fill(display)
    class Button():

        coordy = height/1.5-50

        def __init__(self, coordx,color,name):

            self.coordx = coordx
            self.position = (self.coordx,self.coordy)
            self.color = color
            self.name = name
            self.buttonArea = pg.Rect(width/self.coordx-50,self.coordy,100,100)


        def draw(self):
            """
            desenha botões na tela:
            """
            pg.draw.rect(display,self.color,self.buttonArea)

        def is_hover(self):
            """verifica se o botão foi clicado"""
            mousePosition = pg.mouse.get_pos()
            if self.buttonArea.collidepoint(mousePosition):
                 if pg.mouse.get_pressed()[0] == 1:
                      print(self.name)
                
    
    
    button_pedra = Button(5,(255,0,0),'pedra')
    button_papel = Button(2,(0,255,0),'papel')
    button_tesoura = Button(1.25,(0,0,255),'tesoura')
    
    button_pedra.draw()
    button_papel.draw()
    button_tesoura.draw()

    button_pedra.is_hover()
    button_papel.is_hover()
    button_tesoura.is_hover()


    


    
