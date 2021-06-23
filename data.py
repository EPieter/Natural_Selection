import pygame as pg
import math
from resources import sprites

# initializes pg functions
pg.init()

# url for connection with cloud
url = "http://nsgame.nl/"
app_url = url+"app/"

# from files.data.start_game.py
zoom_level = 0  # range -10, 10
location = [0, 0]  # range (-unlimited, +unlimited), (-unlimited, +unlimited)

# fetches display size

infoObject = pg.display.Info()

# display size
screen = pg.display.set_mode((infoObject.current_w, infoObject.current_h))

# Setup the clock for a decent frame rate
clock = pg.time.Clock()

# from files.data.common_data.py

# define some colors (R, G, B)
WHITE = (255, 255, 255)
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
BGCOLOR = DARKGREY

TILESIZE = 40
GRIDWIDTH = math.ceil(WIDTH / TILESIZE)
GRIDHEIGHT = math.ceil(HEIGHT / TILESIZE)

MIDDLE_OF_THE_SCREEN = [WIDTH / 2, HEIGHT / 2]
MIDDLE_OF_THE_SCREEN_IN_GRIDS = [math.ceil(GRIDWIDTH / 2) - 1, math.ceil(GRIDHEIGHT / 2) - 1]
MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH = MIDDLE_OF_THE_SCREEN_IN_GRIDS[0] - 1
MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT = MIDDLE_OF_THE_SCREEN_IN_GRIDS[1] - 1
img_dir = str(TILESIZE)+"px"







