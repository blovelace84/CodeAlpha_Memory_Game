import pygame
from config import CARD_SIZE

class Card:
    def __init__(self, x, y, symbol):
        self.rect = pygame.Rect(x, y, CARD_SIZE - 5, CARD_SIZE - 5)
        self.symbol = symbol
        self.revealed = False
        self.matched = False

    def draw(self, screen, font, colors):
        if self.revealed or self.matched:
            pygame.draw.rect(screen, colors['green'], self.rect)
            text = font.render(self.symbol, True, colors['black'])
            screen.blit(text,text.get_rect(center=self.rect.center))
        else:
            pygame.draw.rect(screen, colors['gray'], self.rect)