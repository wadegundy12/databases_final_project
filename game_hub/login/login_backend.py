import pygame
import sys

from login.login_format import *
from db import init_db, validate_login, user_exists, create_new_user


class InputBox:
    def __init__(self, x, y, w, h, is_password=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.active = False
        self.is_password = is_password

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                pass
            else:
                self.text += event.unicode

    def draw(self, screen):
        display = self.text if not self.is_password else "*" * len(self.text)
        txt_surface = FONT.render(display, True, NEON_GREEN)
        screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))

        time = pygame.time.get_ticks()
        if self.active and (time // 500) % 2 == 0:  
            cursor_x = self.rect.x + 10 + txt_surface.get_width() + 5
            cursor_y = self.rect.y + 10
            cursor = FONT.render("_", True, NEON_GREEN)
            screen.blit(cursor, (cursor_x, cursor_y))

        pygame.draw.rect(screen, DARK_GREEN, self.rect, 2)


def show_login(screen, player_number):
    init_db()

    clock = pygame.time.Clock()

    username_box = InputBox(200, 175, 300, 60)
    password_box = InputBox(200, 300, 300, 60, is_password=True)

    login_button = pygame.Rect(250, 400, 200, 60)
    join_button = pygame.Rect(250, 480, 200, 60)

    message = ""

    running = True
    while running:
        screen.fill(BLACK)

        title = FONT.render(f"Player {player_number} - Login", True, AMBER)
        screen.blit(title, (90, 50))

        label_user = FONT.render("Username:", True, NEON_GREEN)
        screen.blit(label_user, (200, 115))

        label_pass = FONT.render("Password:", True, NEON_GREEN)
        screen.blit(label_pass, (200, 245))

        username_box.draw(screen)
        password_box.draw(screen)

        pygame.draw.rect(screen, DARK_GRAY, login_button)
        pygame.draw.rect(screen, DARK_GRAY, join_button)

        login_label = FONT.render("Login", True, NEON_GREEN)
        screen.blit(login_label, (login_button.centerx - 90, login_button.centery - 30))

        join_label = FONT.render("Join", True, NEON_GREEN)
        screen.blit(join_label, (join_button.centerx - 75, join_button.centery - 30))

        if message:
            msg_surface = FONT_ERROR_MSG.render(message, True, ERROR_RED)
            screen.blit(msg_surface, (150, 550))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            username_box.handle_event(event)
            password_box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.collidepoint(event.pos):
                    username = username_box.text.strip()
                    password = password_box.text.strip()

                    if validate_login(username, password):
                        return username
                    else:
                        message = "Invalid Login"

                elif join_button.collidepoint(event.pos):
                    username = username_box.text.strip()
                    password = password_box.text.strip()

                    if user_exists(username):
                        message = "Username already exists"
                    elif len(username) < 3 or len(password) < 3:
                        message = "User & pass need 3+ chars"
                    else:
                        create_new_user(username, password)
                        message = "Account created! Log in."

        clock.tick(30)

    return False
