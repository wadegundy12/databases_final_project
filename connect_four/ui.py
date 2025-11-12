# ui.py
import pygame
from constants import BLUE, BLACK, RED, YELLOW, RADIUS, ROWS, COLS, SQUARESIZE, FONT

def draw_board(screen, board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    for c in range(COLS):
        for r in range(ROWS):
            color = RED if board[r][c] == 1 else YELLOW if board[r][c] == 2 else BLACK
            pygame.draw.circle(screen, color, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    pygame.display.update()

def show_winner(screen, piece):
    color = RED if piece == 1 else YELLOW
    label = FONT.render(f"Player {piece} wins!", True, color)
    screen.blit(label, (40, 10))
    pygame.display.update()
