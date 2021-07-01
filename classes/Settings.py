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

        font = pg.font.Font(data.font, 24)
        text = font.render(data.tr.get('Language'), True, data.WHITE_TEXT)
        text_rect = (10, 5, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('State'), True, data.WHITE_TEXT)
        text_rect = (10, 5 + 50, 500, 24)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Dark mode'), True,data.WHITE_TEXT)
        text_rect = (10, 5 + 100, 500, 24)
        self.image.blit(text, text_rect)

    def die(self):
        self.kill()

    def isActive(self):
        return self.alive()
