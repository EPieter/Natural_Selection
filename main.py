import controllers
import functions
from classes import Game

# start the game
#  controllers.start_game()
# controllers.render_engine(data.zoom_level, data.location)
running = True
while running:  # Run until running state changes
    # Creates a thread that runs quit_event()
    controllers.thread.Thread(target=functions.events(), args=(1,), daemon=True)

    # Send log that thread creation is successful
    controllers.thread_function("events", 1)

    # def get_location_from_server():
    #     Server = cloud.Cloud()
    #     Server.get_information()
    #     info = Server.get_variables().data_from_server
    #     list(info)
    #     return info[0]

    # create the game object
    g = Game.Game()
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_go_screen()
