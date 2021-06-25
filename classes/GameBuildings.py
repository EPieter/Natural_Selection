import data
import pygame as pg
from resources import sprites

import functions


class GameBuildings(pg.sprite.Sprite):
    def __init__(self, game, x, y, img_id):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((36, 36), pg.SRCALPHA)
        self.image.convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.image.blit(sprites.menu_items_36[img_id][1], (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = functions.pixelConversionH(x)
        self.rect.y = functions.pixelConversionV(y)
