import pygame as pg
import data


class Settings(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((600, 400))
        self.image.fill(data.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 200

        font = pg.font.Font('Sprites/OpenSans-SemiBold.ttf', 24)

    def die(self):
        self.kill()

    def isActive(self):
        return self.alive()
