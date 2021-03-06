import pygame  # import pygame for PyGame functionality
import sys  # import sys for properly stopping game and other Python Runtime functionality
import time  # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging  # import logging to log things
import common_data as data  # import constant data like colors and sizes
import classes as cl  # import functions en classes (not yet) from classes.py

# initializes PyGame functions
pygame.init()

# sets game to full screen
pygame.display.toggle_fullscreen()

running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    cl.threading.Thread(target=cl.quit_event(), args=(1,), daemon=True)
    # Send log that thread creation is successful
    cl.thread_function("quit_event", 1)

