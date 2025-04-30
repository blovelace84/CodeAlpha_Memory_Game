import pygame

WIDTH, HEIGHT = 800, 600
ROWS, COLS = 4, 4
CARD_SIZE = WIDTH // COLS

#colors
WHITE = (255,255,255)
GRAY = (100,100,100)
GREEN = (0, 200, 0)
BLACK = (0,0,0)

#FONTS
pygame.font.init()
FONT = pygame.font.SysFont(None, 72)