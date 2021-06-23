from classes import Game

# start the game
running = True
while running:  # Run until running state changes

    # create the game object
    g = Game.Game()
    while True:
        g.new()
        g.run()
