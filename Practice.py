import pygame, random

pygame.init()

white = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()

windowHeight = 600
windowWidth = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Move")

carWidth = 100
carHeight = 200
car = pygame.image.load("BlueCar.png")
car = pygame.transform.rotate(car, 90)
car = pygame.transform.scale(car, (carWidth, carHeight))

pygame.mixer.music.load('Sample.mp3')
pygame.mixer.music.play(-1, 0.0)

coinWidth = 50
coinHeight = 100
coin = pygame.image.load("Retro-Coin-icon.png")
coin = pygame.transform.scale(coin, (coinWidth, coinHeight))

bombWidth = 50
bombHeight = 100
bomb = pygame.image.load("big_bomb.png")
bomb = pygame.transform.scale(bomb, (bombWidth, bombHeight))
bombPosy = 0
coinPosy = 0
bombPosx = 0
coinPosx = 0
direction = 'down'

end = False

while not end:
    if direction == 'down':
        bombPosy += 5
        coinPosy += 5

        if bombPosy and coinPosy == 600:
            bombPosy = 0
            coinPosy = 0
            bombPosx = random.randint(0, 800)
            coinPosx = random.randint(0, 800)

            if bombPosx == coinPosx:
                bombPosx = random.randint(0, 800)
                coinPosx = random.randint(0, 800)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            carPosx = mouseX
            carPosy = mouseY

        if event.type == pygame.QUIT or (mouseX, mouseY) == (bombPosx, bombPosy):
            pygame.mixer.music.stop()
            end = True




    window.fill(white)
    window.blit(coin, (coinPosx, coinPosy))
    window.blit(bomb, (bombPosx, bombPosy))
    window.blit(car, (carPosx, carPosy))
    pygame.display.update()

clock.tick(fps)


pygame.quit()
