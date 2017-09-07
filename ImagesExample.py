#This program shows how to display images.

import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Display Example')
clock = pygame.time.Clock()

carImg = pygame.image.load('BlueCar.png')
carImg = pygame.transform.scale(carImg,(200, 100))
carImg = pygame.transform.rotate(carImg, 90)
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

x = (display_width * 0.425)
y = (display_height * 0.65)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        gameDisplay.fill(white)
        car(x, y)
        pygame.display.update()
        clock.tick(30)

pygame.quit()
