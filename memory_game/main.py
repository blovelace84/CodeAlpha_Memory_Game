# main.py

import pygame
import sys
from config import WIDTH, HEIGHT, FONT, WHITE, BLACK, GREEN, GRAY
from utils import generate_cards, draw_board, get_card_at_pos

# Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")
clock = pygame.time.Clock()

# Colors dict for use in card.draw()
colors = {'white': WHITE, 'gray': GRAY, 'green': GREEN, 'black': BLACK}

# Symbols for cards
symbols = list("AABBCCDDEEFFGGHH")
cards = generate_cards(symbols)

# Game state
flipped = []
running = True

# Game loop
while running:
    screen.fill(WHITE)
    draw_board(screen, cards, FONT, colors)
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_card = get_card_at_pos(cards, pos)

            if clicked_card and not clicked_card.revealed and not clicked_card.matched:
                clicked_card.revealed = True
                flipped.append(clicked_card)

                if len(flipped) == 2:
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    if flipped[0].symbol == flipped[1].symbol:
                        flipped[0].matched = True
                        flipped[1].matched = True
                    else:
                        flipped[0].revealed = False
                        flipped[1].revealed = False
                    flipped = []

# Exit
pygame.quit()
sys.exit()
