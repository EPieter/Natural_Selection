import pygame  # import pygame for PyGame functionality
import sys     # import sys for properly stopping game and other Python Runtime functionality
import time    # import time to build delays and pause running code


pygame.init()  # initializes PyGame functions

infoObject = pygame.display.Info()  # fetches display size

# applies display size
pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.toggle_fullscreen()

running = True
while running:  # Run until user asks to quit
    # Makes the ESC key to close the game
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
            sys.exit()













