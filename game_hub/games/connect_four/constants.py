import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6
COLS = 7

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
size = (width, height)

pygame.font.init()
FONT = pygame.font.SysFont("monospace", 60)
SMALL_FONT = pygame.font.SysFont("monospace", 45)
