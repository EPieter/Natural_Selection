import pygame as pg

import threading as thread
import logging as log


# initializes PyGame functions
pg.init()


# from files.controllers.threading.py
# Function used for logging state of thread
def thread_function(thread_name, success_bool):
    if success_bool:
        log.info("Thread %s: successfully started", thread_name)
    else:
        log.error("Thread %s: failed to initialize", thread_name)


# from files.controllers.start_game.py
# function that runs when the game is starting up
def start_game():
    # sets game to full screen
    pg.display.toggle_fullscreen()
    # check_user()
    # TODO: handle every function that needs to start when the games is starting up

