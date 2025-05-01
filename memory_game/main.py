import pygame
import random
from card import Card

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
CARD_SIZE = 100
PADDING = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

colors = {
    'hidden': (100, 100, 100),
    'revealed': (240, 240, 240),
    'matched': (0, 255, 127),
    'text': BLACK
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emoji Memory Game 🎮")
FONT = pygame.font.SysFont("Segoe UI Emoji", 60)
SMALL_FONT = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

# Load sounds
flip_sound = pygame.mixer.Sound("sounds/flip.mp3")
match_sound = pygame.mixer.Sound("sounds/matched.mp3")
win_sound = pygame.mixer.Sound("sounds/win.mp3")

def generate_cards(rows, cols, card_size, padding):
    total_width = cols * card_size + (cols + 1) * padding
    total_height = rows * card_size + (cols + 1) * padding

    start_x = (WIDTH - total_width) // 2 + padding
    start_y = (HEIGHT - total_height) // + padding

    emoji_list = ['🍎', '🚗', '🐶', '🎈', '🌟', '🍕', '🎵', '🧩']
    symbols = emoji_list * 2
    random.shuffle(symbols)
    cards = []

    for row in range(rows):
        row_cards = []
        for col in range(cols):
            x = start_x + col * (card_size + padding) 
            y = start_y + row * (card_size + padding)
            symbol = symbols.pop()
            row_cards.append(Card(x, y, card_size, symbol))
        cards.append(row_cards)
    return cards

def draw_board(surface, cards, font, colors):
    for row in cards:
        for card in row:
            card.draw(surface, font, colors)

def get_card_at_pos(cards, pos):
    for row in cards:
        for card in row:
            if card.rect.collidepoint(pos):
                return card
    return None

def all_matched(cards):
    return all(card.matched for row in cards for card in row)

def draw_restart_button(surface):
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50)
    pygame.draw.rect(surface, GRAY, button_rect)
    pygame.draw.rect(surface, DARK_GRAY, button_rect, 2)
    text = SMALL_FONT.render("Restart", True, BLACK)
    surface.blit(text, text.get_rect(center=button_rect.center))
    return button_rect

def reset_game():
    return generate_cards(ROWS, COLS, CARD_SIZE, PADDING), [], False

# Game state
cards, flipped, played_win_sound = reset_game()
running = True

while running:
    screen.fill(WHITE)
    draw_board(screen, cards, FONT, colors)

    win = all_matched(cards)
    restart_button = None

    if win:
        if not played_win_sound:
            win_sound.play()
            played_win_sound = True
        win_text = FONT.render("You Win! 🎉", True, BLACK)
        screen.blit(win_text, win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
        restart_button = draw_restart_button(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if win and restart_button and restart_button.collidepoint(pos):
                cards, flipped, played_win_sound = reset_game()

            elif not win:
                clicked_card = get_card_at_pos(cards, pos)
                if clicked_card and not clicked_card.revealed and not clicked_card.matched:
                    flip_sound.play()
                    clicked_card.revealed = True
                    flipped.append(clicked_card)

                    if len(flipped) == 2:
                        draw_board(screen, cards, FONT, colors)
                        pygame.display.update()
                        pygame.time.delay(1000)

                        if flipped[0].symbol == flipped[1].symbol:
                            match_sound.play()
                            flipped[0].matched = True
                            flipped[1].matched = True
                        else:
                            flipped[0].revealed = False
                            flipped[1].revealed = False
                        flipped = []

pygame.quit()
