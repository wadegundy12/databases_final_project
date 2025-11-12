# constants.py
import pygame

# Colors (RGB)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Board dimensions
ROWS = 6
COLS = 7

# Square and window sizing
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE  # +1 for top bar
size = (width, height)

# Initialize font system
pygame.font.init()
FONT = pygame.font.SysFont("monospace", 60)
