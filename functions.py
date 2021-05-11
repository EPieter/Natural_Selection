import pygame as pg
import logging as log
import threading as thread
import sys
import os
import requests
import time
import data
import controllers as func


def mouse_events(event):
    if event.type == 4:
        data.zoom_level += 1
        func.render_engine()
    elif event.type == 5:
        data.zoom_level -= 1
        func.render_engine()
    elif event.type == 2:
        data.zoom_level = 0
        func.render_engine()


def second_checker(difference_x_y):
    keyPressed = True
    while keyPressed:
        data.location[0] += difference_x_y[0]
        data.location[1] += difference_x_y[1]
        keyPressed = False


def key_events(event):
    if event.type == pg.K_w:
        second_checker([0, 1])
    elif event.type == pg.K_a:
        second_checker([-1, 0])
    elif event.type == pg.K_s:
        second_checker([0, -1])
    elif event.type == pg.K_d:
        second_checker([1, 0])


def events():
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_events(event)
        elif key_pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        elif event.type == (pg.K_w or pg.K_a or pg.K_s or pg.K_d):
            key_events(event)
