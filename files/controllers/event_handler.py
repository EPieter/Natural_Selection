from .imports import *


# Function that monitors the escape key and terminate program if pressed
def quit_event():
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
