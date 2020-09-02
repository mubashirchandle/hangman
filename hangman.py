import pygame
import os

# Colors
WHITE = (255, 255, 255)

# Setup display
pygame.init()
pygame.display.set_caption('Hangman Game!')
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
images = [pygame.image.load(f'images/hangman{i}.png') for i in range(6)]

# Game variables
hangman_status = 0

# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    # Replace existing hangman image with new one.
    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
