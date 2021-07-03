import data
import pygame as pg


class StoreSelector(pg.sprite.Sprite):
    def __init__(self, store):
        self.groups = store.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = store
        self.image = pg.Surface((300, 76))
        self.image = self.image.convert_alpha()
        self.image.fill((100, 255, 100, 50))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

        self.x_y = 0
        self.x2 = 0
        self.y2 = 0

    def move(self, dx=0, dy=0):
        if 0 <= self.x2 + dx <= 1:
            if 0 <= self.y2 + dy <= 3:
                if self.x_y + dx * 4 + dy <= 6:
                    self.y += dy
                    self.y2 += dy
                    self.x += dx
                    self.x2 += dx
                    self.x_y += dx * 4 + dy

    def update(self):
        self.rect.x = self.x * 300 + data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = self.y * 76 + data.MIDDLE_OF_THE_SCREEN[1] - 304
