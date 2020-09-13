import pygame
import math
import os
import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup display
pygame.init()
pygame.display.set_caption('Hangman Game!')
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
images = [pygame.image.load(f'images/hangman{i}.png') for i in range(7)]

# Button variables
RADIUS = 20
GAP = 15
BUTTON_BOX_WIDTH = (RADIUS * 2 * 13) + (GAP * 12)   # Total width that all the (buttons + gaps) take.
START_X = ((WIDTH - BUTTON_BOX_WIDTH) / 2) + RADIUS # Starting offset for first button
START_Y = 400
letters_pos = []
for i in range(26):
    x = round(START_X + ((RADIUS * 2 + GAP) * (i % 13)))
    y = round(START_Y + ((RADIUS * 2 + GAP) * (i // 13)))
    letters_pos.append([x, y, chr(ord('A') + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

words = ['DEVELOPER', 'PYGAME', 'PYTHON', 'LINUX', 'VSCODE']
FPS = 60
clock = pygame.time.Clock()


def draw(word, guessed, hangman_status):
    win.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render('HANGMAN', 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width()) / 2, 20))

    display_word = ''
    # Draw word
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw alphabet buttons
    for letter_pos in letters_pos:
        x, y, letter, visible = letter_pos

        if not visible:
            continue

        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(letter, 1, BLACK)
        win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Replace existing hangman image with new one.
    win.blit(images[hangman_status], (150, 100))

    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width()) / 2, ((HEIGHT - text.get_height())) / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    # Game variables
    hangman_status = 0
    guessed = []
    WORD = random.choice(words)

    # Reset visibility of all the buttons.
    for letter_pos in letters_pos:
        letter_pos[-1] = True

    # Keep running until either the user wins, loses or closes the game.
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game.
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_x, cur_y = pygame.mouse.get_pos()

                for letter_pos in letters_pos:
                    letter_x, letter_y, letter, visible = letter_pos

                    if not visible:
                        continue

                    # Use the equation of circle (A^2 + B^2 = R^2) to find when a particular button is clicked.
                    distance = math.sqrt(((cur_x - letter_x) ** 2) + ((cur_y - letter_y) ** 2))
                    if distance <= RADIUS:
                        letter_pos[-1] = False
                        guessed.append(letter)
                        if letter not in WORD:
                            hangman_status += 1

        draw(WORD, guessed, hangman_status)

        # If user guessed all the letters correct.
        if set(WORD).issubset(guessed):
            display_message('You WON!')
            break

        if hangman_status == 6:
            display_message('You LOST :(')
            break

    # Return `True` to allow the game to be re-run.
    return True


# Keep running the program until the user presses the close/quit button on the main window.
while main():
    pass
pygame.quit()
