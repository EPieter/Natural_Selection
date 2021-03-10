import files.controllers as func  # import functions en controllers (not yet) from controllers.py


# start the game
func.start_game()

running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    func.thread.Thread(target=func.quit_event(), args=(1,), daemon=True)
    # Send log that thread creation is successful
    func.thread_function("quit_event", 1)

