import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
NEON_GREEN = (57, 255, 20)
LIGHT_GREEN = (0, 255, 120)
DARK_GREEN  = (0, 180, 40)
DARK_GRAY = (50, 50, 50)
AMBER       = (255, 191, 0)
ERROR_RED   = (255, 80, 80)

ROWS = 6
COLS = 7

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)

pygame.font.init()
FONT = pygame.font.SysFont("monospace", 60)
FONT_ERROR_MSG = pygame.font.SysFont("monospace", 30)
