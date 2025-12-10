import pygame
from games.tic_tac_toe.constants import (
    BLACK,
    BLUE,
    RED,
    YELLOW,
    FONT,
    SMALL_FONT,
    GRID_SIZE,
    CELL_SIZE,
    GRID_PIXELS,
    OFFSET_X,
    OFFSET_Y,
    width,
    height,
)


def draw_grid(screen):
    for i in range(1, GRID_SIZE):
        pygame.draw.line(
            screen,
            BLUE,
            (OFFSET_X + i * CELL_SIZE, OFFSET_Y),
            (OFFSET_X + i * CELL_SIZE, OFFSET_Y + GRID_PIXELS),
            6,
        )
        pygame.draw.line(
            screen,
            BLUE,
            (OFFSET_X, OFFSET_Y + i * CELL_SIZE),
            (OFFSET_X + GRID_PIXELS, OFFSET_Y + i * CELL_SIZE),
            6,
        )


def draw_marks(screen, board):
    margin = CELL_SIZE // 5
    thickness = 10

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            mark = board[r][c]
            if mark == 1:
                x0 = OFFSET_X + c * CELL_SIZE + margin
                y0 = OFFSET_Y + r * CELL_SIZE + margin
                x1 = OFFSET_X + (c + 1) * CELL_SIZE - margin
                y1 = OFFSET_Y + (r + 1) * CELL_SIZE - margin
                pygame.draw.line(screen, RED, (x0, y0), (x1, y1), thickness)
                pygame.draw.line(screen, RED, (x0, y1), (x1, y0), thickness)
            elif mark == 2:
                center = (
                    OFFSET_X + c * CELL_SIZE + CELL_SIZE // 2,
                    OFFSET_Y + r * CELL_SIZE + CELL_SIZE // 2,
                )
                radius = CELL_SIZE // 2 - margin
                pygame.draw.circle(screen, YELLOW, center, radius, thickness)


def render_status(screen, current_player, player1, player2):
    screen.fill(BLACK)
    title = FONT.render("Tic Tac Toe", True, BLUE)
    screen.blit(title, (width // 2 - title.get_width() // 2, OFFSET_Y - 110))

    p1_color = RED if current_player == 0 else (150, 150, 150)
    p2_color = YELLOW if current_player == 1 else (150, 150, 150)

    p1_label = SMALL_FONT.render(f"P1: {player1}", True, p1_color)
    p2_label = SMALL_FONT.render(f"P2: {player2}", True, p2_color)

    labels_y = OFFSET_Y - 55
    mid_x = width // 2
    gap = 30

    p1_x = mid_x - gap - p1_label.get_width()
    p2_x = mid_x + gap

    screen.blit(p1_label, (p1_x, labels_y))
    screen.blit(p2_label, (p2_x, labels_y))


def show_end_message(screen, text, color):
    label = FONT.render(text, True, color)
    screen.blit(
        label,
        (width // 2 - label.get_width() // 2, height - 100),
    )
    pygame.display.update()
    pygame.time.wait(2500)
