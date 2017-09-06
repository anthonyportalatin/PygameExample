#This program shows how to create a display

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((920, 720))
pygame.display.set_caption('Display Example')
clock = pygame.time.Clock()

die = False

while not die :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            die = True

        print(event)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
