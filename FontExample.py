import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Font')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

myFont = pygame.font.Font('Chalkboard.ttc', 100)
myFontSurface = myFont.render('Hello World!', True, blue)
myFontRect = myFontSurface.get_rect()
myFontRect.center = (400, 300)

end = False

while not end:
    display.fill(white)
    display.blit(myFontSurface, myFontRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

        pygame.display.update()

pygame.quit()
