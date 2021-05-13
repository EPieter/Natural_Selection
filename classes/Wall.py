import data
import pygame as pg


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((data.TILESIZE, data.TILESIZE))
        self.image.fill(data.GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * data.TILESIZE
        self.rect.y = y * data.TILESIZE
