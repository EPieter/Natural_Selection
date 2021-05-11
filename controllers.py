import pygame as pg
import os
import sys
import threading as thread
import logging as log
import time
import requests as get
import data

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


# from files.controllers.game_map.py
tileSize = 64
screenWidth = data.infoObject.current_w
screenHeight = data.infoObject.current_h


def render_engine(zoom_level=data.zoom_level, location=data.location):
    x = location[0]
    y = location[1]

    gridWidth = screenWidth / tileSize
    gridHeight = screenHeight / tileSize


def draw_grid(self):
    for x in range(0, screenWidth, tileSize):
        pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, screenHeight))
    for y in range(0, screenHeight, tileSize):
        pg.draw.line(self.screen, LIGHTGREY, (0, y), (screenWidth, y))


def draw(self):
    self.screen.fill(77, 68, 68)
    self.draw_grid()
    self.all_sprites.draw(self.screen)
    pg.display.flip()


# from files.controllers.connect_to_cloud.py
# # TODO: needs to run automatically when you start the game
# def check_user():
#     if os.path.exists('../userdata.txt'):
#         f = open('../userdata.txt')
#         file_data = f.read()
#         file_data = file_data.split("|")
#         user = file_data[0]
#         user_pass = file_data[1]
#         url = 'http://nsgame.nl/app/conn.php'
#         url_data_before_sending = {'method': 'get_user_data', 'user': user, 'password': user_pass}
#         x = get.post(url, data=url_data_before_sending)
#
#     else:
#         username = input("username: ")
#         password = input("password: ")
#         file_data_user_do_not_exist(username, password)
#
#     return x.text
#
#
# def file_data_user_do_not_exist(username, password):
#     f = open('../userdata.txt', 'w')
#     f.write(username + "|" + password)
#     url = 'http://nsgame.nl/app/conn.php'
#     url_data_before_sending = {'method': 'check_if_user_exist', 'user': username, 'password': password}
#     x = get.post(url, data=url_data_before_sending)
#     # TODO: ask for creating new user
