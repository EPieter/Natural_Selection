import pygame as pg
import data

availableShortcuts = [
    [data.tr.get("Esc"), data.tr.get("Escape game")],
    [data.tr.get("A or arrow left"), data.tr.get("Move left")],
    [data.tr.get("D or arrow right"), data.tr.get("Move right")],
    [data.tr.get("W or arrow up"), data.tr.get("Move up")],
    [data.tr.get("S or arrow down"), data.tr.get("Move down")],
    [data.tr.get("Space"), data.tr.get("Select and open store")],
    [data.tr.get("Q"), data.tr.get("Close store")],
    [data.tr.get("Left Ctrl"), data.tr.get("Show available shortcuts")],
    [data.tr.get("W or arrow up"), data.tr.get("Select above")],
    [data.tr.get("S or arrow down"), data.tr.get("Select below")],
    [data.tr.get("Return"), data.tr.get("Purchase and place building")],
    [data.tr.get("Delete"), data.tr.get("Delete Building")],
    [data.tr.get("Shift + F1-7"), data.tr.get("Shortcut for placing buildings")],
    [data.tr.get("L"), data.tr.get("Enter dark or light mode")],
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
