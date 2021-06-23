import pygame as pg
import sys
import data



def events():
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()



def pixelConversionH(array_h):
    pixel_h = array_h * data.TILESIZE
    return pixel_h


def pixelConversionV(array_v):
    pixel_v = array_v * data.TILESIZE
    return pixel_v
