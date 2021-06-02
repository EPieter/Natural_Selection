import pygame as pg
import math

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

TILESIZE = 32
GRIDWIDTH = math.ceil(WIDTH / TILESIZE)
GRIDHEIGHT = math.ceil(HEIGHT / TILESIZE)

MIDDLE_OF_THE_SCREEN = [WIDTH / 2, HEIGHT / 2]
MIDDLE_OF_THE_SCREEN_IN_GRIDS = [math.ceil(GRIDWIDTH / 2) - 1, math.ceil(GRIDHEIGHT / 2) - 1]
MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH = MIDDLE_OF_THE_SCREEN_IN_GRIDS[0] - 1
MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT = MIDDLE_OF_THE_SCREEN_IN_GRIDS[1] - 1

img_dir = str(TILESIZE)+"px"
TEXTURE_GRASS01 = pg.image.load("Sprites/" + img_dir + "/Clovers 00 seamless.jpg")
TEXTURE_GRASS02 = pg.image.load("Sprites/" + img_dir + "/Dry_patch_grass_ground_land_dirt_aerial_top_seamless_texture.jpg")
TEXTURE_GRASS03 = pg.image.load("Sprites/" + img_dir + "/Patch grass 00 seamless.jpg")
TEXTURE_GRASS04 = pg.image.load("Sprites/" + img_dir + "/Seamless green grass ground texture.jpg")
TEXTURE_GRASS05 = pg.image.load("Sprites/" + img_dir + "/Seamless wet grass 00.jpg")
TEXTURE_GRASS06 = pg.image.load("Sprites/" + img_dir + "/Seamless green grass ground texture 2.jpg")
TEXTURE_GRASS07 = pg.image.load("Sprites/" + img_dir + "/Seamless long green grass ground texture.jpg")
TEXTURE_GRASS08 = pg.image.load("Sprites/" + img_dir + "/Seamless high res grass texture.jpg")
TEXTURE_GRASS09 = pg.image.load("Sprites/" + img_dir + "/Tileable ground grass texture.jpg")
TEXTURE_GRASS10 = pg.image.load("Sprites/" + img_dir + "/Tileable classic grass texture.jpg")
TEXTURE_GRASS11 = pg.image.load("Sprites/" + img_dir + "/Tileable classic patchy grass texture.jpg")
TEXTURE_GRASS12 = pg.image.load("Sprites/" + img_dir + "/Tileable classic grass and dirt texture.jpg")
TEXTURE_GRASS13 = pg.image.load("Sprites/" + img_dir + "/Grass 00 seamless.jpg")
TEXTURE_GRASS14 = pg.image.load("Sprites/" + img_dir + "/Grass 01 seamless.jpg")
TEXTURE_GRASS15 = pg.image.load("Sprites/" + img_dir + "/Grass 02 seamless.jpg")
TEXTURE_GRASS16 = pg.image.load("Sprites/" + img_dir + "/Grass 03 seamless.jpg")
TEXTURE_GROUND01 = pg.image.load("Sprites/" + img_dir + "/Ground 00 seamless.jpg")
TEXTURE_GROUND02 = pg.image.load("Sprites/" + img_dir + "/Seamless dirt texture.jpg")
TEXTURE_GROUND03 = pg.image.load("Sprites/" + img_dir + "/Seamless ground dirt texture.jpg")
TEXTURE_GROUND04 = pg.image.load("Sprites/" + img_dir + "/Seamless ground dirt texture (1).jpg")
TEXTURE_GROUND05 = pg.image.load("Sprites/" + img_dir + "/Seamless ground texture v1.0.jpg")
TEXTURE_GROUND06 = pg.image.load("Sprites/" + img_dir + "/Seamless hard ground dirt texture.jpg")
TEXTURE_GROUND07 = pg.image.load("Sprites/" + img_dir + "/Seamless hardened dirt ground texture.jpg")
TEXTURE_GROUND08 = pg.image.load("Sprites/" + img_dir + "/Seamless wood chips ground texture.jpg")
TEXTURE_GROUND09 = pg.image.load("Sprites/" + img_dir + "/Tileable ariel ground tiles texture.jpg")
TEXTURE_GROUND10 = pg.image.load("Sprites/" + img_dir + "/Tileable wood chips texture.jpg")
TEXTURE_SAND01 = pg.image.load("Sprites/" + img_dir + "/Fine sand 00 seamless.jpg")
TEXTURE_SAND02 = pg.image.load("Sprites/" + img_dir + "/Seamless beach sand 2 texture.jpg")
TEXTURE_SAND03 = pg.image.load("Sprites/" + img_dir + "/Seamless beach sand.jpg")
TEXTURE_SAND04 = pg.image.load("Sprites/" + img_dir + "/Seamless clay cracks.jpg")
TEXTURE_SAND05 = pg.image.load("Sprites/" + img_dir + "/Seamless desert sand 00.jpg")
TEXTURE_SAND06 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand dirt crack texture.jpg")
TEXTURE_SAND07 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture.jpg")
TEXTURE_SAND08 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture (2).jpg")
TEXTURE_SAND09 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture (3).jpg")
TEXTURE_SAND10 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture (4).jpg")
TEXTURE_SAND11 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture (5).jpg")
TEXTURE_SAND12 = pg.image.load("Sprites/" + img_dir + "/Seamless ground sand texture (6).jpg")
TEXTURE_SAND13 = pg.image.load("Sprites/" + img_dir + "/Seamless light dirt sand ground floor texture.jpg")
TEXTURE_SAND14 = pg.image.load("Sprites/" + img_dir + "/Tileable classic sand texture.jpg")
TEXTURE_SAND15 = pg.image.load("Sprites/" + img_dir + "/Tileable ground sand texture.jpg")
TEXTURE_ROCK01 = pg.image.load("Sprites/" + img_dir + "/Ground stones 00 seamless.jpg")
TEXTURE_ROCK02 = pg.image.load("Sprites/" + img_dir + "/Seamless cobblestones at sunset texture.jpg")
TEXTURE_ROCK03 = pg.image.load("Sprites/" + img_dir + "/Seamless ground rock.jpg")
TEXTURE_ROCK04 = pg.image.load("Sprites/" + img_dir + "/Seamless stones 00.jpg")
TEXTURE_ROCK05 = pg.image.load("Sprites/" + img_dir + "/Seamless limestone rock texture.jpg")
TEXTURE_SNOW01 = pg.image.load("Sprites/" + img_dir + "/Seamless snow 2 texture.jpg")
TEXTURE_SNOW02 = pg.image.load("Sprites/" + img_dir + "/Seamless snow texture.jpg")
TEXTURE_SNOW03 = pg.image.load("Sprites/" + img_dir + "/Seamless snow ground texture.jpg")
TEXTURE_ICE01 = pg.image.load("Sprites/" + img_dir + "/Seamless tileable ice snow cracks ground texture.jpg")



