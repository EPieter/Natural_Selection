"""
This file contains functions and classes (not yet) for the main file
Pure for make it easy to use
"""
# imports
import pygame  # import pygame for PyGame functionality
import sys  # import sys for properly stopping game and other Python Runtime functionality
import time  # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging  # import logging to log things
import common_data as data  # import constant data like colors and sizes

# initializes PyGame functions
pygame.init()


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
        logging.info("Thread %s: successfully started", thread_name)
    else:
        logging.error("Thread %s: failed to initialize", thread_name)
