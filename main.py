import files.controllers as func  # import functions en controllers (not yet) from controllers.py
import files.data as data
import files.classes as c_func

# start the game
func.start_game()

running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    func.thread.Thread(target=c_func.events(), args=(1,), daemon=True)

    # Send log that thread creation is successful
    func.thread_function("events", 1)

    # Frame rate 60fps
    data.clock.tick(60)

