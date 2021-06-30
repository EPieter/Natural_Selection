import data
import pygame as pg
from resources import sprites


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((sprites.TILE_SIZE, sprites.TILE_SIZE))
        self.image.fill(data.WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * data.TILE_SIZE + data.BEGIN_GRID_X + 2
        self.rect.y = self.y * data.TILE_SIZE + data.BEGIN_GRID_Y + 2
