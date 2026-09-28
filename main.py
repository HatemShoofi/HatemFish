import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("HatemFish")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) # Fill the screen with white color
    pygame.display.flip()


pygame.quit()