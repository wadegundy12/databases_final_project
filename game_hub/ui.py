# ui.py
import pygame
from games.connect_four.constants import BLUE, BLACK, RED, YELLOW, RADIUS, ROWS, COLS, SQUARESIZE, FONT

def draw_board(screen, board, player1_name=None, player2_name=None, turn=None):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    for c in range(COLS):
        for r in range(ROWS):
            color = RED if board[r][c] == 1 else YELLOW if board[r][c] == 2 else BLACK
            pygame.draw.circle(screen, color, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

    if player1_name is not None and player2_name is not None:
        # Clear the top row (y from 0 to SQUARESIZE)
        header_rect = pygame.Rect(0, 0, COLS * SQUARESIZE, SQUARESIZE)
        pygame.draw.rect(screen, BLACK, header_rect)

        # Dim the player who is *not* current turn
        p1_color = RED if turn == 0 else (150, 150, 150)
        p2_color = YELLOW if turn == 1 else (150, 150, 150)

        p1_label = FONT.render(f"P1: {player1_name}", True, p1_color)
        p2_label = FONT.render(f"P2: {player2_name}", True, p2_color)

        screen.blit(p1_label, (20, 10))
        screen.blit(p2_label, (COLS * SQUARESIZE // 2 + 20, 10))

    pygame.display.update()

def show_winner(screen, piece, player1_name=None, player2_name=None):
    color = RED if piece == 1 else YELLOW

    if piece == 1 and player1_name:
        text = f"{player1_name} wins!"
    elif piece == 2 and player2_name:
        text = f"{player2_name}  wins!"
    else:
        text = f"Player {piece} wins!"

    label = FONT.render(text, True, color)
    
    header_rect = pygame.Rect(0, 0, COLS * SQUARESIZE, SQUARESIZE)
    pygame.draw.rect(screen, BLACK, header_rect)

    screen.blit(label, (40, 10))
    pygame.display.update()
