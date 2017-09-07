import pygame

pygame.init()

fpsClock = pygame.time.Clock()

display_width = 600
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)

display = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('Hello World!')
car = pygame.image.load('BlueCar.png')
car = pygame.transform.scale(car, (200, 100))
car = pygame.transform.rotate(car, 90)
carx = 0
cary = 500
direction = 'up'
def road(x, y):
    pygame.draw.rect(display, black, (0, 0, 700, 100))
    pygame.draw.rect(display, black, (700, 0, 100, 700))
    pygame.draw.rect(display, black, (0, 500, 700, 100))
    pygame.draw.rect(display, black, (0, 0, 100, 700))

x = 0
y = 0

end = False

while not end:

    if direction == 'up':
        cary -= 5
        if cary == 0:
            direction = 'right'
            car = pygame.transform.rotate(car, -90)

    elif direction == 'right':
        carx += 5
        if carx == 700:
            direction = 'down'
            car = pygame.transform.rotate(car, -90)

    elif direction == 'down':
        cary += 5
        if cary == 500:
            direction ='left'
            car = pygame.transform.rotate(car, -90)

    elif direction == 'left':
        carx -= 5
        if carx == 0:
            direction = 'up'
            car = pygame.transform.rotate(car, -90)
    display.fill(white)
    road(x, y)
    display.blit(car, (carx, cary))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    pygame.display.update()
    fpsClock.tick(60)

pygame.quit()



