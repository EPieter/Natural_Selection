import GameBuildings
import StoreSelector
import data
from classes import Player
from classes import LocalCloud
import functions
import sys
import pygame as pg
from classes import Store
from classes import Shortcuts
from resources import sprites


class Game:
    screen = pg.display.set_mode((data.WIDTH, data.HEIGHT))

    def __init__(self):
        pg.init()

        pg.display.set_caption(data.TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.localCloud = LocalCloud.LocalCloud()
        self.location = self.localCloud.getAllData()
        self.display_surface = None
        # print(self.localCloud.getBuildingsData())
        self.location_x = self.location[0]
        self.location_y = self.location[1]
        # self.location = get_location_from_server()
        self.store = None
        self.shortCuts = None
        self.buildings = []

        self.currentShortcuts = [1, 2, 3, 4, 5, 6, 8, 12]

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player.Player(self, self.location_x, self.location_y)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(data.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        self.localCloud.updateUserData([self.location_x, self.location_y])
        pg.quit()
        sys.exit()

    def move_player(self, dx=0, dy=0):
        location_x = self.location_x
        location_y = self.location_y
        dx = 0 if ((location_x == 0) and (dx == -1)) or ((location_x == (data.GRIDWIDTH - 1)) and (dx == 1)) else dx
        dy = 0 if ((location_y == 0) and (dy == -1)) or ((location_y == (data.GRIDHEIGHT - 1)) and (dy == 1)) else dy
        self.location_x = location_x + dx
        self.location_y = location_y + dy
        self.player.move(dx, dy)

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(data.BGCOLOR)

        self.display_surface = pg.display.set_mode((data.infoObject.current_w, data.infoObject.current_h))

        for y in range(data.GRIDHEIGHT):
            for x in range(data.GRIDWIDTH):
                self.display_surface.blit(data.sprites.TEXTURE_GRASS01,
                                     (functions.pixelConversionH(x), functions.pixelConversionV(y)))
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def updateAvailableShortCuts(self, array_ids):
        self.currentShortcuts = array_ids

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and 1 in self.currentShortcuts:
                    self.quit()
                elif event.key == pg.K_LEFT and 2 in self.currentShortcuts:
                    self.move_player(dx=-1)
                elif event.key == pg.K_RIGHT and 3 in self.currentShortcuts:
                    self.move_player(dx=1)
                elif event.key == pg.K_UP and 4 in self.currentShortcuts:
                    self.move_player(dy=-1)
                elif event.key == pg.K_DOWN and 5 in self.currentShortcuts:
                    self.move_player(dy=1)
                elif event.key == pg.K_a and 2 in self.currentShortcuts:
                    self.move_player(dx=-1)
                elif event.key == pg.K_d and 3 in self.currentShortcuts:
                    self.move_player(dx=1)
                elif event.key == pg.K_w and 4 in self.currentShortcuts:
                    self.move_player(dy=-1)
                elif event.key == pg.K_s and 5 in self.currentShortcuts:
                    self.move_player(dy=1)
                elif event.key == pg.K_SPACE and 6 in self.currentShortcuts:
                    self.show_menu()
                elif event.key == pg.K_q and 7 in self.currentShortcuts:
                    self.close_menu()
                elif event.key == pg.K_LCTRL and 8 in self.currentShortcuts:
                    self.shortCuts = Shortcuts.Shortcuts(self)
                    self.currentShortcuts = [1, 7]

                elif ((event.key == pg.K_w) or (event.key == pg.K_UP)) and 9 in self.currentShortcuts:
                    self.store.selector.move(dy=-1)

                elif ((event.key == pg.K_s) or (event.key == pg.K_DOWN)) and 10 in self.currentShortcuts:
                    self.store.selector.move(dy=1)

                elif event.key == pg.K_SPACE and 11 in self.currentShortcuts:
                    self.close_menu()
                    self.buildings.append(GameBuildings.GameBuildings(self, self.location_x, self.location_y, self.store.selector.x_y))

                elif event.key == pg.K_o and 12 in self.currentShortcuts:
                    pass

    def show_menu(self):
        self.store = Store.Store(self)
        self.currentShortcuts = [1, 7, 8, 9, 10, 11]

    def close_menu(self):
        if self.store is not None:
            if self.store.alive():
                self.currentShortcuts = [1, 2, 3, 4, 5, 6, 8, 12]
                self.store.selector.kill()
                self.store.kill()
        if self.shortCuts is not None:
            if self.shortCuts.alive():
                self.currentShortcuts = [1, 2, 3, 4, 5, 6, 8, 12]
                self.shortCuts.kill()
