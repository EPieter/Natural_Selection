import pygame as pg
import data


class Settings(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((600, 150))
        self.image.fill(data.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = data.MIDDLE_OF_THE_SCREEN[0] - 300
        self.rect.y = data.MIDDLE_OF_THE_SCREEN[1] - 75

        font = pg.font.Font(data.font, 24)
        text = font.render(data.tr.get('Language'), True, data.WHITE_TEXT)
        text_rect = (10, 5, 500, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.lang != "en" else (0, 0, 200)
        text = font.render('EN', True, color)
        text_rect = (10 + 200, 5, 50, 30)
        self.en_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.lang != "nl" else (0, 0, 200)
        text = font.render('NL', True, color)
        text_rect = (10 + 250, 5, 50, 30)
        self.nl_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('State'), True, data.WHITE_TEXT)
        text_rect = (10, 5 + 50, 500, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.state != "us" else (0, 0, 200)
        text = font.render('US', True, color)
        text_rect = (10 + 200, 5 + 50, 50, 30)
        self.us_s_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.state != "uk" else (0, 0, 200)
        text = font.render('UK', True, color)
        text_rect = (10 + 250, 5 + 50, 50, 30)
        self.uk_s_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.state != "nl" else (0, 0, 200)
        text = font.render('NL', True, color)
        text_rect = (10 + 300, 5 + 50, 50, 30)
        self.nl_s_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        color = data.WHITE_TEXT if data.tr.state != "be" else (0, 0, 200)
        text = font.render('BE', True, color)
        text_rect = (10 + 350, 5 + 50, 50, 30)
        self.be_s_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 30, 30)
        self.image.blit(text, text_rect)
        text = font.render(data.tr.get('Dark mode'), True, data.WHITE_TEXT)
        text_rect = (10, 5 + 100, 500, 30)
        self.image.blit(text, text_rect)
        color = (0, 0, 200) if game.dark_mode else data.WHITE_TEXT
        text = font.render(data.tr.get("On"), True, color)
        text_rect = (10 + 200, 5 + 100, 500, 30)
        self.image.blit(text, text_rect)
        self.dark_mode_on_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 45, 30)
        color = (0, 0, 200) if not game.dark_mode else data.WHITE_TEXT
        text = font.render(data.tr.get("Off"), True, color)
        text_rect = (10 + 250, 5 + 100, 500, 30)
        self.image.blit(text, text_rect)
        self.dark_mode_off_rect = (text_rect[0] + self.rect.x, text_rect[1] + self.rect.y, 45, 30)

    def die(self):
        self.kill()

    def isActive(self):
        return self.alive()

    def getElement(self, pos):
        if (self.dark_mode_on_rect[0] < pos[0] < self.dark_mode_on_rect[0] + self.dark_mode_on_rect[2]) and (
                self.dark_mode_on_rect[1] < pos[1] < self.dark_mode_on_rect[1] + self.dark_mode_on_rect[3]) and not self.game.dark_mode:
            self.game.dark_mode = True
            self.game.setDarkMode()

        elif (self.dark_mode_off_rect[0] < pos[0] < self.dark_mode_off_rect[0] + self.dark_mode_off_rect[2]) and (
                self.dark_mode_off_rect[1] < pos[1] < self.dark_mode_off_rect[1] + self.dark_mode_off_rect[3]) and self.game.dark_mode:
            self.game.dark_mode = False
            self.game.setDarkMode()

        elif (self.en_rect[0] < pos[0] < self.en_rect[0] + self.en_rect[2]) and (
                self.en_rect[1] < pos[1] < self.en_rect[1] + self.en_rect[3]) and data.tr.lang != "en":
            data.tr.lang = "en"
            self.game.reloadGame()
        elif (self.nl_rect[0] < pos[0] < self.nl_rect[0] + self.nl_rect[2]) and (
                self.nl_rect[1] < pos[1] < self.nl_rect[1] + self.nl_rect[3]) and data.tr.lang != "nl":
            data.tr.lang = "nl"
            self.game.reloadGame()

        elif (self.nl_s_rect[0] < pos[0] < self.nl_s_rect[0] + self.nl_s_rect[2]) and (
                self.nl_s_rect[1] < pos[1] < self.nl_s_rect[1] + self.nl_s_rect[3]) and data.tr.state != "nl":
            data.tr.state = "nl"
            self.game.reloadGame()

        elif (self.us_s_rect[0] < pos[0] < self.us_s_rect[0] + self.us_s_rect[2]) and (
                self.us_s_rect[1] < pos[1] < self.us_s_rect[1] + self.us_s_rect[3]) and data.tr.state != "us":
            data.tr.state = "us"
            self.game.reloadGame()

        elif (self.uk_s_rect[0] < pos[0] < self.uk_s_rect[0] + self.uk_s_rect[2]) and (
                self.uk_s_rect[1] < pos[1] < self.uk_s_rect[1] + self.uk_s_rect[3]) and data.tr.state != "uk":
            data.tr.state = "uk"
            self.game.reloadGame()

        elif (self.be_s_rect[0] < pos[0] < self.be_s_rect[0] + self.be_s_rect[2]) and (
                self.be_s_rect[1] < pos[1] < self.be_s_rect[1] + self.be_s_rect[3]) and data.tr.state != "be":
            data.tr.state = "be"
            self.game.reloadGame()
