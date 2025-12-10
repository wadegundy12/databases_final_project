import sys
import pygame
from games.connect_four.constants import size, width, height, BLACK, YELLOW, FONT
from menu import show_menu
from login.login_backend import show_login
from games.connect_four.connect4 import run_connect4
from games.tic_tac_toe.tictactoe import run_tictactoe
from leader_board.leaderboard_menu import show_leaderboard_game_menu
from leader_board.leaderboard_view import show_connect4_leaderboard, show_global_leaderboard, show_tictactoe_leaderboard

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)

    player1 = show_login(screen, 1)
    if not player1:
        return

    player2 = show_login(screen, 2)
    if not player2:
        return

    running = True
    while running:
        choice = show_menu(screen, player1, player2)

        if choice == "connect4":
            run_connect4(screen, player1, player2)
        elif choice == "tictactoe":
            run_tictactoe(screen, player1, player2)
        elif choice == "leaderboard":
            game_choice = show_leaderboard_game_menu(screen)

            if game_choice == "connect4":
                show_connect4_leaderboard(screen)
            elif game_choice == "global":
                show_global_leaderboard(screen)
            elif game_choice == "tictactoe":
                show_tictactoe_leaderboard(screen)
        elif choice == "quit" or choice is None:
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
