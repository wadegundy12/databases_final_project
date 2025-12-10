import pygame
import sys
from games.connect_four.constants import BLACK, FONT, size
from login.login_format import NEON_GREEN, AMBER, DARK_GRAY
from db import get_connect4_leaderboard, get_global_leaderboard, get_tictactoe_leaderboard

WIDTH, HEIGHT = size


def show_connect4_leaderboard(screen):
    clock = pygame.time.Clock()
    back_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 100, 300, 60)

    data = get_connect4_leaderboard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return "back"

        screen.fill(BLACK)

        title = FONT.render("Connect4 Rankings", True, AMBER)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 60))

        y = 130
        for i, (user, wins, losses) in enumerate(data[:10], start=1):
            line = FONT.render(f"{i}. {user}  {wins}-{losses}", True, NEON_GREEN)
            screen.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 40

        pygame.draw.rect(screen, DARK_GRAY, back_button, border_radius=10)
        back_text = FONT.render("Back", True, NEON_GREEN)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        pygame.display.flip()
        clock.tick(60)


def show_tictactoe_leaderboard(screen):
    clock = pygame.time.Clock()
    back_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 100, 300, 60)

    data = get_tictactoe_leaderboard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return "back"

        screen.fill(BLACK)

        title = FONT.render("Tic Tac Toe Rankings", True, AMBER)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 60))

        y = 130
        for i, (user, wins, losses) in enumerate(data[:10], start=1):
            line = FONT.render(f"{i}. {user}  {wins}-{losses}", True, NEON_GREEN)
            screen.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 40

        pygame.draw.rect(screen, DARK_GRAY, back_button, border_radius=10)
        back_text = FONT.render("Back", True, NEON_GREEN)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        pygame.display.flip()
        clock.tick(60)

def show_global_leaderboard(screen):
    clock = pygame.time.Clock()
    back_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 100, 300, 60)

    data = get_global_leaderboard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return "back"

        screen.fill(BLACK)

        title = FONT.render("Global Rankings", True, AMBER)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 60))

        y = 130
        for i, (user, wins, losses) in enumerate(data[:10], start=1):
            line = FONT.render(f"{i}. {user}  {wins}-{losses}", True, NEON_GREEN)
            screen.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 40

        pygame.draw.rect(screen, DARK_GRAY, back_button, border_radius=10)
        back_text = FONT.render("Back", True, NEON_GREEN)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        pygame.display.flip()
        clock.tick(60)
