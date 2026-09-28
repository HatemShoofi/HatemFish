import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
White = (255, 255, 255)
Light = (240, 217, 181)
Dark = (181, 136, 99)
SQUARE_SIZE = WIDTH // COLS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HatemFish")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(White) # Fill the screen with white color

    for row in range(ROWS):
        for col in range(COLS):

            color = Light if (row + col) % 2 == 0 else Dark
            Square = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, Square)

    pygame.display.flip()

pygame.quit()