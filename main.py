import os
import base64

appdata = os.getenv("APPDATA")
if not os.path.exists(appdata + "/Natural_Selection/Sprites/install.txt"):
    from classes import Install
    Install.install()
else:
    file = open(appdata + "/Natural_Selection/Sprites/install.txt", "rb")
    file_content = str(base64.urlsafe_b64decode(file.read()), "utf-8")
    if not file_content == "version 1.5.exp":
        from classes import Update

if True:
    from classes import Game

# start the game
running = True
while running:  # Run until running state changes
    # create the game object
    g = Game.Game()
    while True:
        g.new()
        g.run()
