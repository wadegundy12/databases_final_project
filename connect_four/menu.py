# menu.py
import pygame
import sys
from constants import BLACK, BLUE, RED, YELLOW, FONT, size

def draw_button(screen, text, rect, color, hover_color, mouse_pos):
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, rect)
    else:
        pygame.draw.rect(screen, color, rect)

    label = FONT.render(text, True, BLACK)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

def show_menu():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect 4")

    clock = pygame.time.Clock()
    running = True

    play_button = pygame.Rect(220, 250, 300, 80)
    quit_button = pygame.Rect(220, 380, 300, 80)

    while running:
        screen.fill(BLUE)
        title = FONT.render("Connect 4", True, YELLOW)
        screen.blit(title, (200, 100))

        mouse_pos = pygame.mouse.get_pos()
        draw_button(screen, "Play Game", play_button, RED, YELLOW, mouse_pos)
        draw_button(screen, "Quit", quit_button, RED, YELLOW, mouse_pos)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        clock.tick(30)
