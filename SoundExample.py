import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sound')
pygame.mixer.music.load('Sample.mp3')
pygame.mixer.music.play(-1, 0.0)

end = False

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            end = True

        pygame.display.update()

pygame.quit()
