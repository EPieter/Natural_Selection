from .imports import *


def mouse_events(event):
    if event.type == 4:
        func.zoom_in()
    elif event.type == 5:
        func.zoom_out()
    elif event.type == 2:
        func.zoom_reset()


def events():
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_events(event)
        elif key_pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
