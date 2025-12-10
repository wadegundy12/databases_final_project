import pygame
import sys
from games.connect_four.constants import BLACK, FONT, size
from login.login_format import NEON_GREEN, DARK_GRAY, AMBER

WIDTH, HEIGHT = size


def show_leaderboard_game_menu(screen):
    clock = pygame.time.Clock()

    connect4_button = pygame.Rect(WIDTH // 2 - 150, 240, 300, 60)
    back_button     = pygame.Rect(WIDTH // 2 - 150, 340, 300, 60)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if connect4_button.collidepoint(event.pos):
                    return "connect4"
                elif back_button.collidepoint(event.pos):
                    return "back"

        screen.fill(BLACK)

        title = FONT.render("Choose Leaderboard", True, AMBER)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

        pygame.draw.rect(screen, DARK_GRAY, connect4_button, border_radius=10)
        pygame.draw.rect(screen, DARK_GRAY, back_button, border_radius=10)

        c4_label = FONT.render("Connect4", True, NEON_GREEN)
        back_label = FONT.render("Back", True, NEON_GREEN)

        screen.blit(c4_label, c4_label.get_rect(center=connect4_button.center))
        screen.blit(back_label, back_label.get_rect(center=back_button.center))

        pygame.display.flip()
        clock.tick(60)
