import pygame as pg
import math


# initializes pg functions
pg.init()

# fetches display size
infoObject = pg.display.Info()

# display size
screen = pg.display.set_mode((infoObject.current_w, infoObject.current_h))

# Setup the clock for a decent frame rate
clock = pg.time.Clock()

# from files.data.common_data.py

# define some colors (R, G, B)
WHITE = (255, 255, 255)
WHITE_TEXT = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = infoObject.current_w  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = infoObject.current_h  # 16 * 48 or 32 * 24 or 64 * 12
MAX_CALCULATED_AREA_WIDTH = WIDTH + 128
MAX_CALCULATED_AREA_HEIGHT = HEIGHT + 128
FPS = 60
TITLE = "Natural Selection"
BG_COLOR = DARKGREY

TILE_SIZE = 40
GRID_WIDTH = 31
GRID_HEIGHT = 19

MIDDLE_OF_THE_SCREEN = [WIDTH / 2, HEIGHT / 2]
MIDDLE_OF_THE_SCREEN_IN_GRIDS = [math.ceil(GRID_WIDTH / 2) - 1, math.ceil(GRID_HEIGHT / 2) - 1]
MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH = MIDDLE_OF_THE_SCREEN_IN_GRIDS[0] - 1
MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT = MIDDLE_OF_THE_SCREEN_IN_GRIDS[1] - 1

BEGIN_GRID_X = (WIDTH - GRID_WIDTH * TILE_SIZE) / 2
BEGIN_GRID_Y = (HEIGHT - GRID_HEIGHT * TILE_SIZE) / 2

img_dir = str(TILE_SIZE) + "px"
