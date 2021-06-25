import pygame as pg

TILESIZE = 36
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

STORE_SMALL_HOUSE_36 = pg.image.load("Sprites/36px/Small House.png")
STORE_BIG_HOUSE_36 = pg.image.load("Sprites/36px/Big House.png")
STORE_NORMAL_HOUSE_36 = pg.image.load("Sprites/36px/Medium House.png")

menu_items_36 = [
    ["Small house", STORE_SMALL_HOUSE_36],
    ["Big house", STORE_BIG_HOUSE_36],
    ["Normal house", STORE_NORMAL_HOUSE_36],
    # ["Supermarket", pg.image.load("Sprites/72px/.png")],
    # ["Factory", pg.image.load("Sprites/72px/.png")],
]

STORE_SMALL_HOUSE = pg.image.load("Sprites/72px/Small House.png")
STORE_BIG_HOUSE = pg.image.load("Sprites/72px/Big House.png")
STORE_NORMAL_HOUSE = pg.image.load("Sprites/72px/Medium House.png")

menu_items = [
    ["Small house", STORE_SMALL_HOUSE],
    ["Big house", STORE_BIG_HOUSE],
    ["Normal house", STORE_NORMAL_HOUSE],
    # ["Supermarket", pg.image.load("Sprites/72px/.png")],
    # ["Factory", pg.image.load("Sprites/72px/.png")],
]


