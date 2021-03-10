from .imports import *


# Function that monitors the escape key and terminate program if pressed
def quit_event():
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

def mouse_events(event):
    if event.type == 4:
        x = True

def events():
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_events(event)
