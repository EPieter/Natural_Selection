import controllers
import data
import functions

# start the game
controllers.start_game()
controllers.render_engine(data.zoom_level, data.location)
running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    controllers.thread.Thread(target=functions.events(), args=(1,), daemon=True)

    # Send log that thread creation is successful
    controllers.thread_function("events", 1)

    # Frame rate 60fps
    data.clock.tick(60)
