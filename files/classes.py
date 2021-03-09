import pygame  # import pygame for PyGame functionality
import sys  # import sys for properly stopping game and other Python Runtime functionality
import time  # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging as log  # import logging to log things
import files.common_data
import requests  # import for connecting to the cloud
import os  # import for handling files and directories
import files.connect_to_cloud as conn  # import module for connecting to the cloud with functions


# function that runs when the game is starting up
def start_game():
    x = True
    # conn.check_user()
    # TODO: handle every function that needs to start when the games is starting up


# Function that monitors the escape key and terminate program if pressed
def quit_event():
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


# Function used for logging state of thread
def thread_function(thread_name, success_bool):
    if success_bool:
        log.info("Thread %s: successfully started", thread_name)
    else:
        log.error("Thread %s: failed to initialize", thread_name)
