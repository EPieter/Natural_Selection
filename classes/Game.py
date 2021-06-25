import data
from classes import Player
from classes import LocalCloud
import functions
import sys
import pygame as pg
from classes import Store
from classes import Shortcuts


class Game:
    screen = pg.display.set_mode((data.WIDTH, data.HEIGHT))

    def __init__(self):
        pg.init()

        pg.display.set_caption(data.TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.localCloud = LocalCloud.LocalCloud()
        self.location = self.localCloud.getAllData()

        # print(self.localCloud.getBuildingsData())
        self.location_x = self.location[0]
        self.location_y = self.location[1]
        # self.location = get_location_from_server()
        self.store = None
        self.shortCuts = None

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

    def draw_grid(self):
        for x in range(0, data.MAX_CALCULATED_AREA_WIDTH, data.TILESIZE):
            pg.draw.line(self.screen, data.LIGHTGREY, (x, 0), (x, data.HEIGHT))
        for y in range(0, data.MAX_CALCULATED_AREA_HEIGHT, data.TILESIZE):
            pg.draw.line(self.screen, data.LIGHTGREY, (0, y), (data.WIDTH, y))

    def draw(self):
        self.screen.fill(data.BGCOLOR)
        self.draw_grid()
        display_surface = pg.display.set_mode((data.infoObject.current_w, data.infoObject.current_h))

        for y in range(data.GRIDHEIGHT):
            for x in range(data.GRIDWIDTH):
                display_surface.blit(data.sprites.TEXTURE_GRASS01,
                                     (functions.pixelConversionH(x), functions.pixelConversionV(y)))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                elif event.key == pg.K_LEFT:
                    self.move_player(dx=-1)
                elif event.key == pg.K_RIGHT:
                    self.move_player(dx=1)
                elif event.key == pg.K_UP:
                    self.move_player(dy=-1)
                elif event.key == pg.K_DOWN:
                    self.move_player(dy=1)
                elif event.key == pg.K_w:
                    self.move_player(dy=-1)
                elif event.key == pg.K_a:
                    self.move_player(dx=-1)
                elif event.key == pg.K_s:
                    self.move_player(dy=1)
                elif event.key == pg.K_d:
                    self.move_player(dx=1)
                elif event.key == pg.K_SPACE:
                    self.show_menu()
                elif event.key == pg.K_q:
                    if self.store.alive():
                        self.store.die()
                    elif self.shortCuts.alive():
                        self.shortCuts.kill()
                elif event.key == pg.K_LCTRL or pg.K_RCTRL:
                    self.shortCuts = Shortcuts.Shortcuts(self)

    def show_menu(self):
        self.store = Store.Store(self)
