import pygame     # import pygame for PyGame functionality
import sys        # import sys for properly stopping game and other Python Runtime functionality
import time       # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging    # import logging to log things


pygame.init()  # initializes PyGame functions

infoObject = pygame.display.Info()  # fetches display size

# applies display size
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.toggle_fullscreen()


running = True
while running:  # Run until user asks to quit
    def quit_event():                       # TODO: Move this function outside of the while loop
        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

    def thread_function(thread_name, success_bool):         # TODO: Move this function outside of the while loop
        if success_bool:
            logging.info("Thread %s: successfully started", thread_name)
        else:
            logging.info("Thread %s: failed to initialize", thread_name)
    threading.Thread(target=quit_event(), args=(1,), daemon=True)
    thread_function("quit_event", 1)
