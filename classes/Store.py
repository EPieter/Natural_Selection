"""
Store needs to have a gray background
Store needs to have the following items:
    Small house
    Big house
    Normal house
    Supermarket
    Factory
"""

import pygame as pg
import data
from resources import sprites


class Store(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((600, 600))
        self.image.fill(data.LIGHTGREY)
        self.rect = self.image.get_rect()
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 300
        self.menu_items = [
            ["Small house", pg.image.load("Sprites/72px/Small House.png")],
            ["Big house", pg.image.load("Sprites/72px/Big House.png")],
            ["Normal house", pg.image.load("Sprites/72px/Medium House.png")],
            # ["Supermarket", pg.image.load("Sprites/72px/.png")],
            # ["Factory", pg.image.load("Sprites/72px/.png")],
        ]

        for i in range(3):
            for j in range(1):
                self.image.blit(self.menu_items[i][1], (10 + i * 72, 10 + j * 72, 76, 76))

        self.space_between_options = 8

    def addStoreItems(self):
        pass

    def isActive(self):
        return self.alive()
