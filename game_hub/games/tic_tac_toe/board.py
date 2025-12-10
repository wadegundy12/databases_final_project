from games.tic_tac_toe.constants import GRID_SIZE


def create_board():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def check_winner(board):
    lines = []
    lines.extend(board)
    lines.extend([[board[r][c] for r in range(GRID_SIZE)] for c in range(GRID_SIZE)])
    lines.append([board[i][i] for i in range(GRID_SIZE)])
    lines.append([board[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)])

    for line in lines:
        if line[0] and all(cell == line[0] for cell in line):
            return line[0]

    if all(board[r][c] for r in range(GRID_SIZE) for c in range(GRID_SIZE)):
        return "draw"

    return None
