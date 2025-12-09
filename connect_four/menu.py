# menu.py
import pygame
import sys
from constants import BLACK, BLUE, RED, YELLOW, FONT, size
from login_format import NEON_GREEN, DARK_GREEN, LIGHT_GREEN, DARK_GRAY, AMBER

WIDTH, HEIGHT = size

def draw_button(screen, text, rect,
                idle_color, hover_color,
                idle_text_color, hover_text_color,
                mouse_pos):
    if rect.collidepoint(mouse_pos):
        bg_color = hover_color
        text_color = hover_text_color
    else:
        bg_color = idle_color
        text_color = idle_text_color

    pygame.draw.rect(screen, bg_color, rect, border_radius=10)

    label = FONT.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


def show_menu(screen, player1, player2):
    clock = pygame.time.Clock()

    # Buttons (centered horizontally)
    connect4_button = pygame.Rect(WIDTH // 2 - 150, 220, 300, 60)
    ttt_button      = pygame.Rect(WIDTH // 2 - 150, 320, 300, 60) 
    leaderboard_button = pygame.Rect(WIDTH // 2 - 150, 420, 300, 60) 
    quit_button     = pygame.Rect(WIDTH // 2 - 150, 520, 300, 60)

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
                elif leaderboard_button.collidepoint(event.pos):
                    return "leaderboard"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # ----- draw screen -----
        screen.fill(BLACK)

        # Title
        title = FONT.render("Choose a Game", True, AMBER)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        subtitle = FONT.render(f"{player1} vs {player2}", True, LIGHT_GREEN)
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

        # Buttons
        draw_button(
            screen, "Connect4", connect4_button,
            DARK_GRAY, NEON_GREEN,    
            NEON_GREEN, BLACK,         
            mouse_pos
        )

        draw_button(
            screen, "Game TBA", ttt_button,
            DARK_GRAY, NEON_GREEN,
            NEON_GREEN, BLACK,
            mouse_pos
        )

        draw_button(
            screen, "TopDogs", leaderboard_button,
            DARK_GRAY, NEON_GREEN,
            NEON_GREEN, BLACK,
            mouse_pos
        )

        draw_button(
            screen, "Quit", quit_button,
            (120, 0, 0), (200, 0, 0), 
            (255, 255, 255), (255, 255, 255),  
            mouse_pos
        )

        pygame.display.flip()
        clock.tick(60)
