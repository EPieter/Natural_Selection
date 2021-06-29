import pygame as pg
from classes import Translate as tr
import data

availableShortcuts = [
    [tr.get("Esc"), tr.get("Escape game")],
    [tr.get("A or arrow left"), tr.get("Move left")],
    [tr.get("D or arrow right"), tr.get("Move right")],
    [tr.get("W or arrow up"), tr.get("Move up")],
    [tr.get("S or arrow down"), tr.get("Move down")],
    [tr.get("Space"), tr.get("Select and open store")],
    [tr.get("Q"), tr.get("Close store")],
    [tr.get("Left Ctrl"), tr.get("Show available shortcuts")],
    [tr.get("W or arrow up"), tr.get("Select above")],
    [tr.get("S or arrow down"), tr.get("Select below")],
    [tr.get("Return"), tr.get("Purchase and place building")],
    [tr.get("Delete"), tr.get("Delete Building")],
    [tr.get("Shift + F1-7"), tr.get("Shortcut for placing buildings")],
    [tr.get("L"), tr.get("Enter dark or light mode")],
]


class Shortcuts(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((600, 400))
        self.image.fill(data.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 200
        self.shortCuts = []
        self.shortCuts.append(["Q", "Close popup"])
        for i in self.game.currentShortcuts:
            self.shortCuts.append(availableShortcuts[i - 1])

        font = pg.font.Font('Sprites/OpenSans-SemiBold.ttf', 24)
        for i in range(len(self.shortCuts)):
            text = font.render((self.shortCuts[i][0]), True, (255, 255, 255))
            text_rect = (10 + 0 * 76, 10 + i * 32, 500, 24)
            self.image.blit(text, text_rect)
            text = font.render((self.shortCuts[i][1]), True, (255, 255, 255))
            text_rect = (10 + 3 * 76, 10 + i * 32, 500, 24)
            self.image.blit(text, text_rect)

    def die(self):
        self.kill()

    def isActive(self):
        return self.alive()
