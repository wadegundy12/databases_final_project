# login.py
import pygame
import sys
from constants import BLACK, BLUE, RED, YELLOW, FONT, size
from db import init_db, validate_login, user_exists, create_new_user


# ----------------------
# Text Input Class
# ----------------------
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
        pygame.draw.rect(screen, YELLOW if self.active else RED, self.rect, 2)
        display_text = (
            "*" * len(self.text) if self.is_password else self.text
        )
        text_surface = FONT.render(display_text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


# ----------------------
# Login Screen
# ----------------------
def show_login(screen):
    init_db()

    clock = pygame.time.Clock()

    username_box = InputBox(200, 200, 300, 50)
    password_box = InputBox(200, 300, 300, 50, is_password=True)

    login_button = pygame.Rect(250, 400, 200, 60)
    create_button = pygame.Rect(250, 480, 200, 60)

    message = ""

    running = True
    while running:
        screen.fill(BLUE)

        title = FONT.render("Login", True, YELLOW)
        screen.blit(title, (260, 120))

        label_user = FONT.render("Username:", True, BLACK)
        screen.blit(label_user, (200, 170))

        label_pass = FONT.render("Password:", True, BLACK)
        screen.blit(label_pass, (200, 270))

        username_box.draw(screen)
        password_box.draw(screen)

        # Buttons
        pygame.draw.rect(screen, RED, login_button)
        pygame.draw.rect(screen, RED, create_button)

        login_label = FONT.render("Login", True, BLACK)
        screen.blit(login_label, (login_button.centerx - 40, login_button.centery - 15))

        create_label = FONT.render("Create Account", True, BLACK)
        screen.blit(create_label, (create_button.centerx - 110, create_button.centery - 15))

        # Message text
        if message:
            msg_surface = FONT.render(message, True, BLACK)
            screen.blit(msg_surface, (200, 550))

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
                        return True
                    else:
                        message = "Invalid username or password"

                elif create_button.collidepoint(event.pos):
                    username = username_box.text.strip()
                    password = password_box.text.strip()

                    if user_exists(username):
                        message = "Username already exists"
                    elif len(username) < 3 or len(password) < 3:
                        message = "Username and password must be 3+ chars"
                    else:
                        create_new_user(username, password)
                        message = "Account created! Log in now."

        clock.tick(30)

    return False
