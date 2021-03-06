import pygame     # import pygame for PyGame functionality
import sys        # import sys for properly stopping game and other Python Runtime functionality
import time       # import time to build delays and pause running code
import threading  # import threading for running multiple functions at once
import logging    # import logging to log things

# initializes PyGame functions
pygame.init()

# fetches display size
infoObject = pygame.display.Info()

# applies display size
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.toggle_fullscreen()

# define commonly used colors, textures and icons
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
TEXTURE_GRASS01 = pygame.image.load("/Sprites/Clovers 00 seamless.jpg")
TEXTURE_GRASS02 = pygame.image.load("/Sprites/Dry_patch_grass_ground_land_dirt_aerial_top_seamless_texture.jpg")
TEXTURE_GRASS03 = pygame.image.load("/Sprites/Patch grass 00 seamless.jpg")
TEXTURE_GRASS04 = pygame.image.load("/Sprites/Seamless green grass ground texture.jpg")
TEXTURE_GRASS05 = pygame.image.load("/Sprites/Seamless wet grass 00.jpg")
TEXTURE_GRASS06 = pygame.image.load("/Sprites/Seamless green grass ground texture 2.jpg")
TEXTURE_GRASS07 = pygame.image.load("/Sprites/Seamless long green grass ground texture.jpg")
TEXTURE_GRASS08 = pygame.image.load("/Sprites/Seamless high res grass texture.jpg")
TEXTURE_GRASS09 = pygame.image.load("/Sprites/Tileable ground grass texture.jpg")
TEXTURE_GRASS10 = pygame.image.load("/Sprites/Tileable classic grass texture.jpg")
TEXTURE_GRASS11 = pygame.image.load("/Sprites/Tileable classic patchy grass texture.jpg")
TEXTURE_GRASS12 = pygame.image.load("/Sprites/Tileable classic grass and dirt texture.jpg")
TEXTURE_GRASS13 = pygame.image.load("/Sprites/Grass 00 seamless.jpg")
TEXTURE_GRASS14 = pygame.image.load("/Sprites/Grass 01 seamless.jpg")
TEXTURE_GRASS15 = pygame.image.load("/Sprites/Grass 02 seamless.jpg")
TEXTURE_GRASS16 = pygame.image.load("/Sprites/Grass 03 seamless.jpg")
TEXTURE_GROUND01 = pygame.image.load("/Sprites/Ground 00 seamless.jpg")
TEXTURE_GROUND02 = pygame.image.load("/Sprites/Seamless dirt texture.jpg")
TEXTURE_GROUND03 = pygame.image.load("/Sprites/Seamless ground dirt texture.jpg")
TEXTURE_GROUND04 = pygame.image.load("/Sprites/Seamless ground dirt texture (1).jpg")
TEXTURE_GROUND05 = pygame.image.load("/Sprites/Seamless ground texture v1.0.jpg")
TEXTURE_GROUND06 = pygame.image.load("/Sprites/Seamless hard ground dirt texture.jpg")
TEXTURE_GROUND07 = pygame.image.load("/Sprites/Seamless hardened dirt ground texture.jpg")
TEXTURE_GROUND08 = pygame.image.load("/Sprites/Seamless wood chips ground texture.jpg")
TEXTURE_GROUND09 = pygame.image.load("/Sprites/Tileable ariel ground tiles texture.jpg")
TEXTURE_GROUND10 = pygame.image.load("/Sprites/Tileable wood chips texture.jpg")
TEXTURE_SAND01 = pygame.image.load("/Sprites/Fine sand 00 seamless.jpg")
TEXTURE_SAND02 = pygame.image.load("/Sprites/Seamless beach sand 2 texture.jpg")
TEXTURE_SAND03 = pygame.image.load("/Sprites/Seamless beach sand.jpg")
TEXTURE_SAND04 = pygame.image.load("/Sprites/Seamless clay cracks.jpg")
TEXTURE_SAND05 = pygame.image.load("/Sprites/Seamless desert sand 00.jpg")
TEXTURE_SAND06 = pygame.image.load("/Sprites/Seamless ground sand dirt crack texture.jpg")
TEXTURE_SAND07 = pygame.image.load("/Sprites/Seamless ground sand texture.jpg")
TEXTURE_SAND08 = pygame.image.load("/Sprites/Seamless ground sand texture (2).jpg")
TEXTURE_SAND09 = pygame.image.load("/Sprites/Seamless ground sand texture (3).jpg")
TEXTURE_SAND10 = pygame.image.load("/Sprites/Seamless ground sand texture (4).jpg")
TEXTURE_SAND11 = pygame.image.load("/Sprites/Seamless ground sand texture (5).jpg")
TEXTURE_SAND12 = pygame.image.load("/Sprites/Seamless ground sand texture (6).jpg")
TEXTURE_SAND13 = pygame.image.load("/Sprites/Seamless light dirt sand ground floor texture.jpg")
TEXTURE_SAND14 = pygame.image.load("/Sprites/Tileable classic sand texture.jpg")
TEXTURE_SAND15 = pygame.image.load("/Sprites/Tileable ground sand texture.jpg")
TEXTURE_ROCK01 = pygame.image.load("/Sprites/Ground stones 00 seamless.jpg")
TEXTURE_ROCK02 = pygame.image.load("/Sprites/Seamless cobblestones at sunset texture.jpg")
TEXTURE_ROCK03 = pygame.image.load("/Sprites/Seamless ground rock.jpg")
TEXTURE_ROCK04 = pygame.image.load("/Sprites/Seamless stones 00.jpg")
TEXTURE_ROCK05 = pygame.image.load("/Sprites/Seamless limestone rock texture.jpg")
TEXTURE_SNOW01 = pygame.image.load("/Sprites/Seamless snow 2 texture.jpg")
TEXTURE_SNOW02 = pygame.image.load("/Sprites/Seamless snow texture.jpg")
TEXTURE_SNOW03 = pygame.image.load("/Sprites/Seamless snow ground texture.jpg")
TEXTURE_ICE01 = pygame.image.load("/Sprites/Seamless tileable ice snow cracks ground texture.jpg")


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

