import pygame as pg

import data

availableShortcuts = [
    ["Esc", "Escape game"],
    ["A or ArrowLeft", "Move left"],
    ["D or ArrowRight", "Move right"],
    ["W or ArrowUp", "Move up"],
    ["S or ArrowDown", "Move down"],
    ["Space", "Select and open store"],
    ["Q", "Quit store"],
]
currentShortcuts = []


class Shortcuts(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((400, 400))
        self.image.fill(data.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 200
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 200

        self.space_between_options = 8

    def die(self):
        self.kill()

    def isActive(self):
        return self.alive()
