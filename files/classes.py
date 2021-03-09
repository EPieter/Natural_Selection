"""
This file contains functions and classes (not yet) for the main file
"""
from imports import * # this module contains every module

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
        log.info("Thread %s: successfully started", thread_name)
    else:
        log.error("Thread %s: failed to initialize", thread_name)
