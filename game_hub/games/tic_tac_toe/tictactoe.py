import sys
import pygame
from games.tic_tac_toe.constants import (
    GRID_SIZE,
    CELL_SIZE,
    GRID_PIXELS,
    OFFSET_X,
    OFFSET_Y,
    BLUE,
    RED,
    YELLOW,
)
from games.tic_tac_toe.board import create_board, check_winner
from games.tic_tac_toe.ui import render_status, draw_grid, draw_marks, show_end_message
from db import record_result


def run_tictactoe(screen, player1, player2):
    board = create_board()
    current_player = 0
    running = True

    while running:
        render_status(screen, current_player, player1, player2)
        draw_grid(screen)
        draw_marks(screen, board)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (
                    OFFSET_X <= x < OFFSET_X + GRID_PIXELS
                    and OFFSET_Y <= y < OFFSET_Y + GRID_PIXELS
                ):
                    col = (x - OFFSET_X) // CELL_SIZE
                    row = (y - OFFSET_Y) // CELL_SIZE

                    if board[row][col] == 0:
                        piece = 1 if current_player == 0 else 2
                        board[row][col] = piece

                        result = check_winner(board)
                        if result:
                            render_status(screen, current_player, player1, player2)
                            draw_grid(screen)
                            draw_marks(screen, board)
                            pygame.display.update()

                            if result == "draw":
                                show_end_message(screen, "Draw game!", BLUE)
                            else:
                                winner = player1 if result == 1 else player2
                                loser = player2 if result == 1 else player1
                                record_result("tictactoe", winner, loser)
                                color = RED if result == 1 else YELLOW
                                show_end_message(screen, f"{winner} wins!", color)
                            running = False
                        else:
                            current_player = 1 - current_player
        if not running:
            return
