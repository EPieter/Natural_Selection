import pygame
import sys


# Function that monitors the escape key and terminate program if pressed
def quit_event():
    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
