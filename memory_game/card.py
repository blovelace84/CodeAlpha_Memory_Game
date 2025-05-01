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
        else:
            pygame.draw.rect(surface, colors['hidden'], self.rect)

        pygame.draw.rect(surface, colors['text'], self.rect, 2)

        if self.revealed or self.matched:
            text = font.render(self.symbol, True, colors['text'])
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)