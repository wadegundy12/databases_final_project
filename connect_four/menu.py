# menu.py
import pygame
import sys
from constants import BLACK, BLUE, RED, YELLOW, FONT, size

WIDTH, HEIGHT = size


def draw_button(screen, text, rect, color, hover_color, mouse_pos):
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, rect, border_radius=10)
    else:
        pygame.draw.rect(screen, color, rect, border_radius=10)

    label = FONT.render(text, True, BLACK)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


def show_menu(screen, player1, player2):
    """
    Show the game-select menu.
    Returns a string like: "connect4", "tictactoe", or None (if quit).
    """
    clock = pygame.time.Clock()

    # Buttons (centered horizontally)
    connect4_button = pygame.Rect(WIDTH // 2 - 150, 220, 300, 60)
    ttt_button      = pygame.Rect(WIDTH // 2 - 150, 320, 300, 60)  
    quit_button     = pygame.Rect(WIDTH // 2 - 150, 420, 300, 60)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if connect4_button.collidepoint(event.pos):
                    return "connect4"
                elif ttt_button.collidepoint(event.pos):
                    return "tictactoe"  
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # ----- draw screen -----
        screen.fill(BLACK)

        # Title
        title = FONT.render("Choose a Game", True, YELLOW)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        subtitle = FONT.render(f"{player1} vs {player2}", True, BLUE)
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

        # Buttons
        draw_button(screen, "Connect Four", connect4_button, BLUE, YELLOW, mouse_pos)
        draw_button(screen, "Coming Soon", ttt_button, BLUE, YELLOW, mouse_pos)
        draw_button(screen, "Quit",        quit_button, RED,  YELLOW, mouse_pos)

        pygame.display.flip()
        clock.tick(60)
