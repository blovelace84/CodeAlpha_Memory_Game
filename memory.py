import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
CARD_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (160, 160, 160)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont(None, 60)

# Symbols (could be emojis or letters)
symbols = list("AABBCCDDEEFFGGHH")
random.shuffle(symbols)

# Cards data
cards = []
for row in range(ROWS):
    for col in range(COLS):
        rect = pygame.Rect(col * CARD_SIZE, row * CARD_SIZE, CARD_SIZE, CARD_SIZE)
        index = row * COLS + col
        cards.append({'rect': rect, 'symbol': symbols[index], 'revealed': False, 'matched': False})

# Game state
flipped = []
running = True

# Game loop
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for card in cards:
                if card['rect'].collidepoint(pos) and not card['revealed'] and not card['matched']:
                    card['revealed'] = True
                    flipped.append(card)
                    if len(flipped) == 2:
                        pygame.time.wait(500)
                        if flipped[0]['symbol'] == flipped[1]['symbol']:
                            flipped[0]['matched'] = True
                            flipped[1]['matched'] = True
                        else:
                            flipped[0]['revealed'] = False
                            flipped[1]['revealed'] = False
                        flipped = []

    # Draw cards
    for card in cards:
        if card['revealed'] or card['matched']:
            pygame.draw.rect(screen, GREEN, card['rect'])
            text = font.render(card['symbol'], True, (0, 0, 0))
            text_rect = text.get_rect(center=card['rect'].center)
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, GRAY, card['rect'])

    pygame.display.flip()

pygame.quit()
sys.exit()
