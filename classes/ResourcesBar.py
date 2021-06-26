import pygame as pg

import data


class ResourcesBar(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((data.WIDTH, 50), pg.SRCALPHA)
        self.image.convert_alpha()
        self.image.fill((255, 255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.money = game.money
        self.people = game.people_in_the_city
        self.level = game.level
        self.production = game.production
        font = pg.font.Font('resources/OpenSans-SemiBold.ttf', 24)
        text = font.render('Production: ' + str(format(self.production, ".2f")), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx - 400
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render('Money: € ' + str(format(self.money, ".2f")), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx - 150
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render('People: ' + str(self.people), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx + 100
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)
        text = font.render('Press Ctrl for all shortcuts', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.image.get_rect().centerx + 400
        text_rect.centery = self.image.get_rect().centery
        self.image.blit(text, text_rect)


