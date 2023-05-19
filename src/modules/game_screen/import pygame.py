import pygame
pygame.init()
width = 600
height = 500
screen = pygame.display.set_mode((width, height))
image = pygame.image.load('src/sprites/full_heart.png')
image_2 = pygame.image.load('src/sprites/full_heart.png')
img = pygame.transform.scale(image, (35, 35))
img_2 = pygame.transform.scale(image_2, (35,35))

while True:
    screen.fill("white")
    screen.blit(image, (0,0)) 
    screen.blit(image_2, (40,0))
    #pular a width de 20 em 20, manter a height em 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()