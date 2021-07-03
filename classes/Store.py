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
        font = pg.font.Font(data.font, 18)
        color_pr = (200, 0, 0)
        color_max = (0, 200, 0)
        color_p = (0, 0, 200)
        text = font.render(data.tr.get('Money'), True, data.WHITE_TEXT)
        text_rect = (10 + 0 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('People'), True, color_p)
        text_rect = (10 + 1 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Production') + ' ' + data.ToolStore.moneySymbol() + '/sp', True, color_pr)
        text_rect = (10 + 2 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Limit workers'), True, color_max)
        text_rect = (10 + 4 * 76, 5, 500, 24)
        self.image.blit(text, text_rect)
        font = pg.font.Font(data.font, 20)
        for i in range(2):
            for j in range(4):
                if i * 4 + j < 7:
                    self.image.blit(sprites.menu_items[i * 4 + j][1], (10 + i * 300, 38 + j * 76, 76, 76))
                    price = sprites.menu_items[i * 4 + j][2] if sprites.menu_items[i * 4 + j][
                                                                    0] != "Bitcoin" else float(game.bitcoin_price)
                    text = font.render(
                        data.ToolStore.moneySymbol() + ' ' + data.ToolStore.priceFormatterIncludeCalc(price), True,
                        data.WHITE_TEXT)
                    text_rect = (10 + 1.2 * 76 + i * 300, 40 + j * 76, 500, 24)
                    self.image.blit(text, text_rect)
                    if sprites.menu_items[i * 4 + j][3] != 0:
                        text = font.render(
                            str(sprites.menu_items[i * 4 + j][3]) + " " + data.tr.get("persons").capitalize(), True,
                            color_p)
                        text_rect = (10 + 1.2 * 76 + i * 300, 62 + j * 76, 500, 24)
                        self.image.blit(text, text_rect)
                        if sprites.menu_items[i * 4 + j][4] != 0:
                            text = font.render(
                                str(data.ToolStore.priceFormatterIncludeCalc(sprites.menu_items[j][4],
                                                                             ",.3f")) + ' ' + data.ToolStore.moneySymbol() + '/sp',
                                True,
                                color_pr)
                            text_rect = (10 + 1.2 * 76 + i * 300, 84 + j * 76, 500, 24)
                            self.image.blit(text, text_rect)
                        elif sprites.menu_items[i * 4 + j][5] != 0:
                            text = font.render(str(sprites.menu_items[i * 4 + j][5]) + " " + data.tr.get("workers").capitalize(), True, color_max)
                            text_rect = (10 + 1.2 * 76 + i * 300, 84 + j * 76, 500, 24)
                            self.image.blit(text, text_rect)
                    elif sprites.menu_items[i * 4 + j][4] != 0:
                        text = font.render(
                            str(data.ToolStore.priceFormatterIncludeCalc(sprites.menu_items[i * 4 + j][4],
                                                                         ",.3f")) + ' ' + data.ToolStore.moneySymbol() + '/sp',
                            True, color_pr)
                        text_rect = (10 + 1.2 * 76 + i * 300, 62 + j * 76, 500, 24)
                        self.image.blit(text, text_rect)
                        if sprites.menu_items[i * 4 + j][5] != 0:
                            text = font.render(str(sprites.menu_items[i * 4 + j][5]) + " " + data.tr.get("workers").capitalize(), True, color_max)
                            text_rect = (10 + 1.2 * 76 + i * 300, 84 + j * 76, 500, 24)
                            self.image.blit(text, text_rect)
                    elif sprites.menu_items[i * 4 + j][5] != 0:
                        text = font.render(str(sprites.menu_items[i * 4 + j][5]) + " " + data.tr.get("workers").capitalize(), True, color_max)
                        text_rect = (10 + 1.2 * 76 + i * 300, 62 + j * 76, 500, 24)
                        self.image.blit(text, text_rect)

    def isActive(self):
        return self.alive()
