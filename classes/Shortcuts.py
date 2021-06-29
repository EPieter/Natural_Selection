import pygame as pg
from classes import Translate as tr
import data

availableShortcuts = [
    [tr.selectLang("nl", "Esc"), tr.selectLang("nl", "Escape game")],
    [tr.selectLang("nl", "A or arrow left"), tr.selectLang("nl", "Move left")],
    [tr.selectLang("nl", "D or arrow right"), tr.selectLang("nl", "Move right")],
    ["W or ArrowUp", "Move up"],
    ["S or ArrowDown", "Move down"],
    ["Space", "Select and open store"],
    ["Q", "Close store"],
    ["Left Ctrl", "Show available shortcuts"],
    ["W or ArrowUp", "Select above"],
    ["D or ArrowDown", "Select below"],
    ["Return", "Purchase and place building"],
    ["Delete", "Delete Building"],
    ["Shift + F1-7", "Shortcut for placing buildings"],
    ["L", "Enter dark or light mode"],
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
