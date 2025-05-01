import pygame

class Card:
    def __init__(self, x, y, size, symbol):
        self.rect = pygame.Rect(x, y, size, size)
        self.symbol = symbol
        self.revealed = False
        self.matched = False

    def draw(self, surface, font, colors):
        if self.matched:
            pygame.draw.rect(surface, colors['matched'], self.rect)
        elif self.revealed:
            pygame.draw.rect(surface, colors['revealed'], self.rect)
            text = font.render(self.symbol, True, colors['text'])
            surface.blit(text, text.get_rect(center=self.rect.center))
        else:
            pygame.draw.rect(surface, colors['hidden'], self.rect)