import pygame  # import pygame for PyGame functionality
import sys  # import sys for properly stopping game and other Python Runtime functionality
import time  # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging  # import logging to log things
import data  # import constant data like colors and files

# initializes PyGame functions
pygame.init()

# fetches display size
infoObject = pygame.display.Info()

# applies display size
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.toggle_fullscreen()


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


running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    threading.Thread(target=quit_event(), args=(1,), daemon=True)
    # Send log that thread creation is successful
    thread_function("quit_event", 1)
