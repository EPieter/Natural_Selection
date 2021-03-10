"""
This file contains common data that is necessary for Natural Selection
"""
from .imports import *

# initializes pg functions
pg.init()


# define commonly used colors, textures and icons
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

TEXTURE_GRASS01 = pg.image.load("Sprites/Clovers 00 seamless.jpg")
TEXTURE_GRASS02 = pg.image.load("Sprites/Dry_patch_grass_ground_land_dirt_aerial_top_seamless_texture.jpg")
TEXTURE_GRASS03 = pg.image.load("Sprites/Patch grass 00 seamless.jpg")
TEXTURE_GRASS04 = pg.image.load("Sprites/Seamless green grass ground texture.jpg")
TEXTURE_GRASS05 = pg.image.load("Sprites/Seamless wet grass 00.jpg")
TEXTURE_GRASS06 = pg.image.load("Sprites/Seamless green grass ground texture 2.jpg")
TEXTURE_GRASS07 = pg.image.load("Sprites/Seamless long green grass ground texture.jpg")
TEXTURE_GRASS08 = pg.image.load("Sprites/Seamless high res grass texture.jpg")
TEXTURE_GRASS09 = pg.image.load("Sprites/Tileable ground grass texture.jpg")
TEXTURE_GRASS10 = pg.image.load("Sprites/Tileable classic grass texture.jpg")
TEXTURE_GRASS11 = pg.image.load("Sprites/Tileable classic patchy grass texture.jpg")
TEXTURE_GRASS12 = pg.image.load("Sprites/Tileable classic grass and dirt texture.jpg")
TEXTURE_GRASS13 = pg.image.load("Sprites/Grass 00 seamless.jpg")
TEXTURE_GRASS14 = pg.image.load("Sprites/Grass 01 seamless.jpg")
TEXTURE_GRASS15 = pg.image.load("Sprites/Grass 02 seamless.jpg")
TEXTURE_GRASS16 = pg.image.load("Sprites/Grass 03 seamless.jpg")
TEXTURE_GROUND01 = pg.image.load("Sprites/Ground 00 seamless.jpg")
TEXTURE_GROUND02 = pg.image.load("Sprites/Seamless dirt texture.jpg")
TEXTURE_GROUND03 = pg.image.load("Sprites/Seamless ground dirt texture.jpg")
TEXTURE_GROUND04 = pg.image.load("Sprites/Seamless ground dirt texture (1).jpg")
TEXTURE_GROUND05 = pg.image.load("Sprites/Seamless ground texture v1.0.jpg")
TEXTURE_GROUND06 = pg.image.load("Sprites/Seamless hard ground dirt texture.jpg")
TEXTURE_GROUND07 = pg.image.load("Sprites/Seamless hardened dirt ground texture.jpg")
TEXTURE_GROUND08 = pg.image.load("Sprites/Seamless wood chips ground texture.jpg")
TEXTURE_GROUND09 = pg.image.load("Sprites/Tileable ariel ground tiles texture.jpg")
TEXTURE_GROUND10 = pg.image.load("Sprites/Tileable wood chips texture.jpg")
TEXTURE_SAND01 = pg.image.load("Sprites/Fine sand 00 seamless.jpg")
TEXTURE_SAND02 = pg.image.load("Sprites/Seamless beach sand 2 texture.jpg")
TEXTURE_SAND03 = pg.image.load("Sprites/Seamless beach sand.jpg")
TEXTURE_SAND04 = pg.image.load("Sprites/Seamless clay cracks.jpg")
TEXTURE_SAND05 = pg.image.load("Sprites/Seamless desert sand 00.jpg")
TEXTURE_SAND06 = pg.image.load("Sprites/Seamless ground sand dirt crack texture.jpg")
TEXTURE_SAND07 = pg.image.load("Sprites/Seamless ground sand texture.jpg")
TEXTURE_SAND08 = pg.image.load("Sprites/Seamless ground sand texture (2).jpg")
TEXTURE_SAND09 = pg.image.load("Sprites/Seamless ground sand texture (3).jpg")
TEXTURE_SAND10 = pg.image.load("Sprites/Seamless ground sand texture (4).jpg")
TEXTURE_SAND11 = pg.image.load("Sprites/Seamless ground sand texture (5).jpg")
TEXTURE_SAND12 = pg.image.load("Sprites/Seamless ground sand texture (6).jpg")
TEXTURE_SAND13 = pg.image.load("Sprites/Seamless light dirt sand ground floor texture.jpg")
TEXTURE_SAND14 = pg.image.load("Sprites/Tileable classic sand texture.jpg")
TEXTURE_SAND15 = pg.image.load("Sprites/Tileable ground sand texture.jpg")
TEXTURE_ROCK01 = pg.image.load("Sprites/Ground stones 00 seamless.jpg")
TEXTURE_ROCK02 = pg.image.load("Sprites/Seamless cobblestones at sunset texture.jpg")
TEXTURE_ROCK03 = pg.image.load("Sprites/Seamless ground rock.jpg")
TEXTURE_ROCK04 = pg.image.load("Sprites/Seamless stones 00.jpg")
TEXTURE_ROCK05 = pg.image.load("Sprites/Seamless limestone rock texture.jpg")
TEXTURE_SNOW01 = pg.image.load("Sprites/Seamless snow 2 texture.jpg")
TEXTURE_SNOW02 = pg.image.load("Sprites/Seamless snow texture.jpg")
TEXTURE_SNOW03 = pg.image.load("Sprites/Seamless snow ground texture.jpg")
TEXTURE_ICE01 = pg.image.load("Sprites/Seamless tileable ice snow cracks ground texture.jpg")

# fetches display size
infoObject = pg.display.Info()

# display size
screen = pg.display.set_mode((infoObject.current_w, infoObject.current_h))
