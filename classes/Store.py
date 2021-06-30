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
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 340
        self.selector = StoreSelector.StoreSelector(game)
        font = pg.font.Font('Sprites/OpenSans-SemiBold.ttf', 18)
        text = font.render(data.tr.get('Money'), True, data.WHITE_TEXT)
        text_rect = (10 + 1.5 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('People'), True, data.WHITE_TEXT)
        text_rect = (10 + 3 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Production') + ' ' + data.Tools.moneySymbol() + '/sp', True, data.WHITE_TEXT)
        text_rect = (10 + 4 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Limit workers'), True, data.WHITE_TEXT)
        text_rect = (10 + 6 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        font = pg.font.Font('Sprites/OpenSans-SemiBold.ttf', 20)
        for i in range(1):
            for j in range(7):
                self.image.blit(sprites.menu_items[j][1], (10 + i * 76, 38 + j * 76, 76, 76))
                text = font.render(data.Tools.moneySymbol() + ' ' + str(sprites.menu_items[j][2]), True, data.WHITE_TEXT)
                text_rect = (10 + 1.5 * 76, 68 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][3]), True, data.WHITE_TEXT) if sprites.menu_items[j][3] != 0 else font.render("n/a", True, data.WHITE_TEXT)
                text_rect = (10 + 3 * 76, 68 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][4]), True, data.WHITE_TEXT) if sprites.menu_items[j][4] != 0 else font.render("n/a", True, data.WHITE_TEXT)
                text_rect = (10 + 4 * 76, 68 + j * 76, 500, 24)
                self.image.blit(text, text_rect)
                text = font.render(str(sprites.menu_items[j][5]), True, data.WHITE_TEXT) if sprites.menu_items[j][5] != 0 else font.render("n/a", True, data.WHITE_TEXT)
                text_rect = (10 + 6 * 76, 68 + j * 76, 500, 24)
                self.image.blit(text, text_rect)

    def isActive(self):
        return self.alive()





