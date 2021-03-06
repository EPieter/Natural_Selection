import pygame as pg

import data


class ResourcesBar(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((data.WIDTH, 50), pg.SRCALPHA)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.money = game.money
        self.people = game.people_in_the_city
        self.production = game.production
        font = pg.font.Font(data.font, 24)
        text = font.render(data.tr.get('Production') + ": " + data.ToolStore.priceFormatterIncludeCalc(self.production) + " " + data.ToolStore.moneySymbol() + "/s", True, data.DARKGREY)
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx - 420
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Money') + ": " + data.ToolStore.moneySymbol() + " " + data.ToolStore.priceFormatterIncludeCalc(self.money), True, data.DARKGREY)
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx - 150
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('People') + ": " + str(self.people), True, data.DARKGREY)
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx + 100
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Press ctrl for all shortcuts'), True, data.DARKGREY)
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx + 400
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)


