import controllers
from data import *
import functions
import sys
from sprites import *
from classes import ClassCloud as cloud

# start the game
#  controllers.start_game()
# controllers.render_engine(data.zoom_level, data.location)
running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    controllers.thread.Thread(target=functions.events(), args=(1,), daemon=True)

    # Send log that thread creation is successful
    controllers.thread_function("events", 1)


    def get_location_from_server():
        Server = cloud.UserInformation()
        Server.get_information()
        info = Server.get_variables().data_from_server
        list(info)
        return info[0]


    class Game:
        def __init__(self):
            pg.init()
            self.screen = pg.display.set_mode((WIDTH, HEIGHT))
            pg.display.set_caption(TITLE)
            self.clock = pg.time.Clock()
            pg.key.set_repeat(500, 100)
            self.load_data()
            self.location = [MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH, MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT]
            # self.location = get_location_from_server()

        def load_data(self):
            pass

        def new(self):
            # initialize all variables and do all the setup for a new game
            self.all_sprites = pg.sprite.Group()
            self.walls = pg.sprite.Group()
            self.player = Player(self, MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH, MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT)
            for x in range(10, 20):
                Wall(self, x, 5)

        def run(self):
            # game loop - set self.playing = False to end the game
            self.playing = True
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000
                self.events()
                self.update()
                self.draw()

        def quit(self):
            pg.quit()
            sys.exit()

        def move_player(self, dx=0, dy=0):
            current_location = self.location
            location_x = current_location[0]
            location_y = current_location[1]
            dx = 0 if ((location_x == 0) and (dx == -1)) or ((location_x == (GRIDWIDTH - 1)) and (dx == 1)) else dx
            dy = 0 if ((location_y == 0) and (dy == -1)) or ((location_y == (GRIDHEIGHT - 1)) and (dy == 1)) else dy

            new_location = [location_x + dx, location_y + dy]
            self.location = new_location
            self.player.move(dx, dy)

        def update(self):
            # update portion of the game loop
            self.all_sprites.update()

        def update_user_data(self):
            pass

        def draw_grid(self):
            for x in range(0, MAX_CALCULATED_AREA_WIDTH, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
            for y in range(0, MAX_CALCULATED_AREA_HEIGHT, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        def draw(self):
            self.screen.fill(BGCOLOR)
            self.draw_grid()
            self.all_sprites.draw(self.screen)
            pg.display.flip()

        def events(self):
            # catch all events here
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.update_user_data()
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.update_user_data()
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
                        # second_checker([0, 1])
                    elif event.key == pg.K_a:
                        self.move_player(dx=-1)
                        # second_checker([-1, 0])
                    elif event.key == pg.K_s:
                        self.move_player(dy=1)
                        # second_checker([0, -1])
                    elif event.key == pg.K_d:
                        self.move_player(dx=1)
                        # second_checker([1, 0])

        def show_start_screen(self):
            pass

        def show_go_screen(self):
            pass


    # create the game object
    g = Game()
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_go_screen()

