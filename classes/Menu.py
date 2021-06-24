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
from Game import Game


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

        self.menu = None
        self.menu_items = [
            ["Small house", pg.image.load("Sprites/normal/Clovers 00 seamless.jpg")],
            ["Big house", pg.image.load("Sprites/normal/Clovers 00 seamless.jpg")],
            ["Normal house", pg.image.load("Sprites/normal/Clovers 00 seamless.jpg")],
            ["Supermarket", pg.image.load("Sprites/normal/Clovers 00 seamless.jpg")],
            ["Factory", pg.image.load("Sprites/normal/Clovers 00 seamless.jpg")],
        ]
        self.space_between_options = 8

    def addStoreItems(self):
        pass
