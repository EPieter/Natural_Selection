from files.imports import *  # import all modules

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

