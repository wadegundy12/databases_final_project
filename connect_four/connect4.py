import sys
import pygame
from constants import *
from board import *
from ui import *
from db import record_result

def run_connect4(screen, player1, player2):
    board = create_board()
    game_over = False
    turn = 0  
    
    draw_board(screen, board, player1, player2, turn)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                color = RED if turn == 0 else YELLOW
                pygame.draw.circle(screen, color, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                col = int(posx / SQUARESIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)

                    piece = 1 if turn == 0 else 2
                    drop_piece(board, row, col, piece)

                    if winning_move(board, piece):
                        if piece == 1:
                            winner = player1
                            loser = player2
                        else:
                            winner = player2
                            loser = player1

                        record_result("connect4",winner, loser)


                        show_winner(screen, piece, player1, player2)
                        game_over = True
                    else:
                        turn = (turn + 1) % 2
                        
                    draw_board(screen, board, player1, player2, turn)

        if game_over:
            pygame.time.wait(3000)
            return