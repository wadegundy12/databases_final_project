import pygame
import sys
from games.connect_four.constants import BLACK, FONT, SMALL_FONT, size
from login.login_format import NEON_GREEN, DARK_GRAY, AMBER

WIDTH, HEIGHT = size


def show_leaderboard_game_menu(screen):
    clock = pygame.time.Clock()

    global_button   = pygame.Rect(WIDTH // 2 - 150, 200, 300, 60)
    connect4_button = pygame.Rect(WIDTH // 2 - 150, 300, 300, 60)
    ttt_button      = pygame.Rect(WIDTH // 2 - 150, 400, 300, 60)
    back_button     = pygame.Rect(WIDTH // 2 - 150, 500, 300, 60)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if global_button.collidepoint(event.pos):
                    return "global"
                elif connect4_button.collidepoint(event.pos):
                    return "connect4"
                elif ttt_button.collidepoint(event.pos):
                    return "tictactoe"
                elif back_button.collidepoint(event.pos):
                    return "back"

        screen.fill(BLACK)

        title = FONT.render("Choose Leaderboard", True, AMBER)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

        pygame.draw.rect(screen, DARK_GRAY, global_button, border_radius=10)
        pygame.draw.rect(screen, DARK_GRAY, connect4_button, border_radius=10)
        pygame.draw.rect(screen, DARK_GRAY, ttt_button, border_radius=10)
        pygame.draw.rect(screen, DARK_GRAY, back_button, border_radius=10)

        c4_label = FONT.render("Connect4", True, NEON_GREEN)
        global_label = FONT.render("Global", True, NEON_GREEN)
        ttt_label = SMALL_FONT.render("TicTacToe", True, NEON_GREEN)
        back_label = FONT.render("Back", True, NEON_GREEN)

        screen.blit(c4_label, c4_label.get_rect(center=connect4_button.center))
        screen.blit(global_label, global_label.get_rect(center=global_button.center))
        screen.blit(ttt_label, ttt_label.get_rect(center=ttt_button.center))
        screen.blit(back_label, back_label.get_rect(center=back_button.center))

        pygame.display.flip()
        clock.tick(60)
