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

from classes import StoreSelector
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
        self.selector = StoreSelector.StoreSelector(game)
        font = pg.font.Font('resources/OpenSans-SemiBold.ttf', 18)
        text = font.render('Money', True, (255, 255, 255))
        text_rect = (10 + 1.5 * 76, 10, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render('People', True, (255, 255, 255))
        text_rect = (10 + 3 * 76, 10, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render('Production €/sp', True, (255, 255, 255))
        text_rect = (10 + 4 * 76, 10, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render('Limit workers', True, (255, 255, 255))
        text_rect = (10 + 6 * 76, 10, 500, 24)
        self.image.blit(text, text_rect)
        font = pg.font.Font('resources/OpenSans-SemiBold.ttf', 20)
        for i in range(1):
            for j in range(7):
                self.image.blit(sprites.menu_items[j][1], (10 + i * 76, 34 + j * 76, 76, 76))
                text = font.render('€ ' + str(sprites.menu_items[j][2]), True, (255, 255, 255))
                text_rect = (10 + 1.5 * 76, 64 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][3]), True, (255, 255, 255)) if sprites.menu_items[j][3] != 0 else font.render("n/a", True, (255, 255, 255))
                text_rect = (10 + 3 * 76, 64 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][4]), True, (255, 255, 255)) if sprites.menu_items[j][4] != 0 else font.render("n/a", True, (255, 255, 255))
                text_rect = (10 + 4 * 76, 64 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][5]), True, (255, 255, 255)) if sprites.menu_items[j][5] != 0 else font.render("n/a", True, (255, 255, 255))
                text_rect = (10 + 6 * 76, 64 + j * 76, 500, 24)
                self.image.blit(text, text_rect)

    def addStoreItems(self):
        pass

    def isActive(self):
        return self.alive()





