import pygame as pg

TILESIZE = 36
img_dir = str(TILESIZE)+"px"

TEXTURE_GRASS01 = pg.image.load("Sprites/" + img_dir + "/Clovers 00 seamless.jpg")

STORE_SMALL_HOUSE_36 = pg.image.load("Sprites/36px/Small House.png")
STORE_BIG_HOUSE_36 = pg.image.load("Sprites/36px/Big House.png")
STORE_NORMAL_HOUSE_36 = pg.image.load("Sprites/36px/Medium House.png")
STORE_SMALL_FACTORY_36 = pg.image.load("Sprites/36px/Small Factory.png")
STORE_BIG_FACTORY_36 = pg.image.load("Sprites/36px/Big Factory.png")
STORE_DIAMOND_36 = pg.image.load("Sprites/36px/Diamond.png")
STORE_BITCOIN_36 = pg.image.load("Sprites/36px/Bitcoin.png")

menu_items_36 = [
    ["Small house", STORE_SMALL_HOUSE_36, 50],
    ["Normal house", STORE_NORMAL_HOUSE_36, 100],
    ["Big house", STORE_BIG_HOUSE_36, 200],
    ["Small Factory", STORE_SMALL_FACTORY_36],
    ["Big Factory", STORE_BIG_FACTORY_36],
    ["Bitcoin", STORE_BITCOIN_36],
    ["Diamond", STORE_DIAMOND_36],
]

STORE_SMALL_HOUSE = pg.image.load("Sprites/72px/Small House.png")
STORE_BIG_HOUSE = pg.image.load("Sprites/72px/Big House.png")
STORE_NORMAL_HOUSE = pg.image.load("Sprites/72px/Medium House.png")
STORE_SMALL_FACTORY = pg.image.load("Sprites/72px/Small Factory.png")
STORE_BIG_FACTORY = pg.image.load("Sprites/72px/Big Factory.png")
STORE_BITCOIN = pg.image.load("Sprites/72px/Bitcoin.png")
STORE_DIAMOND = pg.image.load("Sprites/72px/Diamond.png")

menu_items = [
    ["Small house", STORE_SMALL_HOUSE, 50, 3, 0, 0],
    ["Normal house", STORE_NORMAL_HOUSE, 100, 7, 0, 0],
    ["Big house", STORE_BIG_HOUSE, 200, 15, 0, 0],
    ["Small Factory", STORE_SMALL_FACTORY, 500, 0, 0.05, 20],
    ["Big Factory", STORE_BIG_FACTORY, 1200, 0, 1, 100],
    ["Bitcoin", STORE_BITCOIN, 50000, 0, 0, 0],
    ["Diamond", STORE_DIAMOND, 1000000, 0, 0, 0],
]


