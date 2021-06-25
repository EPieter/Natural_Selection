import data
import pygame as pg


class StoreSelector(pg.sprite.Sprite):
    def __init__(self, store):
        self.groups = store.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = store
        self.image = pg.Surface((600, 76))
        self.image = self.image.convert_alpha()
        self.image.fill((255, 0, 0, 50))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

        self.x_y = 0

    def move(self, dy=0):
        if self.x_y + dy >= 0:
            if self.x_y + dy <= 2:
                self.y += dy
                self.x_y += dy

    def update(self):
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = self.y * 72 + data.MIDDLE_OF_THE_SCREEN[1] - 290
