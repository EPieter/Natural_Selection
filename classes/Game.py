from classes import GameBuildings
from classes import ResourcesBar
import data
from classes import Player
from classes import LocalCloud
import functions
import sys
import pygame as pg
from classes import Store
from classes import Shortcuts
from resources import sprites
from classes import Settings
import time
import urllib.request
import json


class Game:
    screen = pg.display.set_mode((data.WIDTH, data.HEIGHT))

    def __init__(self):

        self.playing = True
        pg.init()
        pg.display.set_caption(data.TITLE)
        self.clock = pg.time.Clock()
        pg.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
        pg.key.set_repeat(500, 100)
        self.localCloud = LocalCloud.LocalCloud()
        self.userdata = self.localCloud.getAllData()
        data.tr.lang = self.userdata['lang']
        data.tr.state = self.userdata['state']
        self.location = self.userdata['location']
        self.display_surface = None
        self.location_x = self.location[0]
        self.location_y = self.location[1]
        self.store = None
        self.shortCuts = None
        self.settings = None
        self.buildings = []
        self.saved_buildings = self.userdata['buildings']
        self.currentShortcuts = [1, 2, 3, 4, 5, 6, 8, 12, 13, 15]
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player.Player(self, self.location_x, self.location_y)

        self.dt = self.clock.tick(data.FPS) / 1000
        self.people_in_the_city = self.userdata['people']
        self.money = self.userdata['money']
        self.createBuildings()
        self.calculateProduction()
        self.resources = ResourcesBar.ResourcesBar(self)
        self.time1 = time.time()
        self.time2 = None
        self.time_switch = True
        self.dark_mode = self.userdata['dark_mode']
        self.setDarkMode()
        self.bitcoin_price = 50000
        self.counter_btc = 500
        self.url_btc = "https://api.nomics.com/v1/currencies/ticker?key=0a9d6b39d77c59f71d722322ecec7630a7b5ed25" \
                       "&ids=BTC,ETH,XRP&interval=1d,30d&convert=BUSD&per-page=100&page=1 "
        self.updateBitcoin(force=True)

    def new(self):
        # initialize all variables and do all the setup for a new game
        pass

    def run(self):
        # game loop - set self.playing = False to end the game
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.updateMoney()

    def quit(self):
        saveBuildings = []
        for buildings in self.buildings:
            cache = []
            for items in range(3):
                cache.append(buildings[items])
            saveBuildings.append(cache)

        self.buildings = saveBuildings
        self.localCloud.updateUserData(self)
        pg.quit()
        sys.exit()

    def move_player(self, dx=0, dy=0):
        location_x = self.location_x
        location_y = self.location_y
        dx = 0 if ((location_x == 0) and (dx == -1)) or ((location_x == (data.GRID_WIDTH - 1)) and (dx == 1)) else dx
        dy = 0 if ((location_y == 0) and (dy == -1)) or ((location_y == (data.GRID_HEIGHT - 1)) and (dy == 1)) else dy
        self.location_x = location_x + dx
        self.location_y = location_y + dy
        self.player.move(dx, dy)

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(data.BG_COLOR)

        self.display_surface = pg.display.set_mode((data.infoObject.current_w, data.infoObject.current_h))
        self.display_surface.fill(data.WHITE)
        for y in range(data.GRID_HEIGHT):
            for x in range(data.GRID_WIDTH):
                self.display_surface.blit(sprites.TEXTURE_GRASS01,
                                          (functions.pixelConversionH(x), functions.pixelConversionV(y)))
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and 1 in self.currentShortcuts:
                    self.quit()
                elif ((event.key == pg.K_a) or (event.key == pg.K_LEFT)) and 2 in self.currentShortcuts:
                    self.move_player(dx=-1)
                elif ((event.key == pg.K_d) or (event.key == pg.K_RIGHT)) and 3 in self.currentShortcuts:
                    self.move_player(dx=1)
                elif ((event.key == pg.K_w) or (event.key == pg.K_UP)) and 4 in self.currentShortcuts:
                    self.move_player(dy=-1)
                elif ((event.key == pg.K_s) or (event.key == pg.K_DOWN)) and 5 in self.currentShortcuts:
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

                elif event.key == pg.K_RETURN and 11 in self.currentShortcuts:
                    price = sprites.menu_items[self.store.selector.x_y][2] if self.store.selector.x_y != 5 else float(
                        self.bitcoin_price)
                    if self.money >= price:
                        self.buildings.append([self.location_x, self.location_y, self.store.selector.x_y,
                                               GameBuildings.GameBuildings(self, self.location_x, self.location_y,
                                                                           self.store.selector.x_y)])
                        self.money -= price
                        self.people_in_the_city += sprites.menu_items[self.store.selector.x_y][3]
                        self.calculateProduction()
                    self.close_menu()

                elif event.key == pg.K_DELETE and 12 in self.currentShortcuts:
                    for i in self.buildings:
                        if i[0] == self.location_x:
                            if i[1] == self.location_y:
                                i[3].kill()
                                self.people_in_the_city -= sprites.menu_items[i[2]][3]
                                if sprites.menu_items[i[2]][0] == "Bitcoin":
                                    self.money += float(self.bitcoin_price)
                                else:
                                    self.money += sprites.menu_items[i[2]][2] / 2
                                self.buildings.remove(i)
                                self.calculateProduction()
                    self.reloadGame()
                elif event.key == pg.K_F1 and 15 in self.currentShortcuts:
                    self.settings = Settings.Settings(self)
                    self.currentShortcuts = [1, 7, 16]
                    pg.mouse.set_cursor(*pg.cursors.arrow)
                    pg.key.set_repeat(500, 100)
                    pg.mouse.set_pos(data.MIDDLE_OF_THE_SCREEN)

                if 13 in self.currentShortcuts:
                    all_keys = pg.key.get_pressed()
                    if (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F1]:
                        self.createBuilding(0)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F2]:
                        self.createBuilding(1)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F3]:
                        self.createBuilding(2)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F4]:
                        self.createBuilding(3)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F5]:
                        self.createBuilding(4)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F6]:
                        self.createBuilding(5)
                    elif (all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]) and all_keys[pg.K_F7]:
                        self.createBuilding(6)
            if event.type == pg.MOUSEBUTTONUP and 16 in self.currentShortcuts:
                self.settings.getElement(pg.mouse.get_pos())

    def show_menu(self):
        run = True
        if self.buildings:
            for building in self.buildings:
                if (building[0] == self.location_x) and (building[1] == self.location_y):
                    run = False

        if run:
            self.store = Store.Store(self)
            self.currentShortcuts = [1, 7, 8, 9, 10, 11]

    def close_menu(self):
        shortcuts = [1, 2, 3, 4, 5, 6, 8, 12, 13, 15]
        if self.shortCuts is not None:
            if self.shortCuts.alive():
                if self.store is not None:
                    if self.store.alive():
                        self.currentShortcuts = [1, 7, 8, 9, 10, 11]
                    else:
                        self.currentShortcuts = shortcuts
                else:
                    self.currentShortcuts = shortcuts
                self.shortCuts.kill()
                self.shortCuts = None
        elif self.store is not None:
            if self.store.alive():
                self.currentShortcuts = shortcuts
                self.store.selector.kill()
                self.store.kill()
                self.store = None
        elif self.settings is not None:
            if self.settings.alive():
                self.currentShortcuts = shortcuts
                self.settings.kill()
                self.settings = None
                pg.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
                pg.key.set_repeat(500, 100)

    def createBuildings(self):

        for buildings in self.saved_buildings:
            self.buildings.append([buildings[0], buildings[1], buildings[2],
                                   GameBuildings.GameBuildings(self, buildings[0], buildings[1], buildings[2])])

    def updateMoney(self):
        pg.time.wait(20)
        if self.time_switch:
            self.time2 = time.time()
            time_diff = abs(self.time2 - self.time1)
            self.time_switch = False
        else:
            self.time1 = time.time()
            time_diff = abs(self.time1 - self.time2)
            self.time_switch = True
        self.money += self.production * time_diff
        self.resources.kill()
        self.resources = ResourcesBar.ResourcesBar(self)
        self.updateBitcoin()

    def calculateProduction(self):
        buildings = self.buildings
        buildings.sort(key=lambda x: x[2], reverse=True)
        self.production = 0
        people = self.people_in_the_city
        for factory in buildings:
            limit = sprites.menu_items[factory[2]][5]
            production = sprites.menu_items[factory[2]][4]
            if people - limit > 0:
                people -= limit
                self.production += limit * production
            else:
                self.production += people * production
                people = 0

    def createBuilding(self, key):
        price = sprites.menu_items[key][2] if key != 5 else float(self.bitcoin_price)
        if self.money >= price:
            run = True
            if self.buildings:
                for building in self.buildings:
                    if (building[0] == self.location_x) and (building[1] == self.location_y):
                        run = False
            if run:
                self.buildings.append([self.location_x, self.location_y, key,
                                       GameBuildings.GameBuildings(self, self.location_x, self.location_y,
                                                                   key)])
                self.money -= price
                self.people_in_the_city += sprites.menu_items[key][3]
                self.calculateProduction()

    def setDarkMode(self):
        if self.dark_mode:
            data.WHITE = (40, 40, 40)
            data.DARKGREY = (255, 255, 255)
            data.GREEN = (0, 100, 0)
        else:
            data.DARKGREY = (40, 40, 40)
            data.WHITE = (255, 255, 255)
            data.GREEN = (0, 200, 0)
        self.reloadGame()

    def reloadGame(self):
        self.currentShortcuts = [1, 2, 3, 4, 5, 6, 8, 12, 13, 15]
        if self.store is not None:
            if self.store.alive():
                self.store.selector.kill()
                self.store.kill()
                self.store = Store.Store(self)
                self.currentShortcuts = [1, 7, 8, 9, 10, 11]
        if self.shortCuts is not None:
            if self.shortCuts.alive():
                self.shortCuts.kill()
                self.shortCuts = Shortcuts.Shortcuts(self)
                self.currentShortcuts = [1, 7]
        if self.settings is not None:
            if self.settings.alive():
                self.settings.kill()
                self.settings = Settings.Settings(self)
                self.currentShortcuts = [1, 7, 16]

    def updateBitcoin(self, force=False):
        if self.counter_btc > 0 and not force:
            self.counter_btc -= 1
        else:
            self.counter_btc = 1000
            self.bitcoin_price = json.loads(urllib.request.urlopen(self.url_btc).read())[0]["price"]
