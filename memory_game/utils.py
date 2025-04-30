# utils.py

from card import Card
from config import ROWS, COLS, CARD_SIZE
import random

def generate_cards(symbols):
    random.shuffle(symbols)
    cards = []
    for row in range(ROWS):
        row_cards = []
        for col in range(COLS):
            index = row * COLS + col
            x = col * CARD_SIZE
            y = row * CARD_SIZE
            card = Card(x, y, symbols[index])
            row_cards.append(card)
        cards.append(row_cards)
    return cards

def draw_board(screen, cards, font, colors):
    for row in cards:
        for card in row:
            card.draw(screen, font, colors)

def get_card_at_pos(cards, pos):
    for row in cards:
        for card in row:
            if card.rect.collidepoint(pos):
                return card
    return None
