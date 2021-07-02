import os
import base64


def Update():
    print("Updating...")
    appdata = os.getenv("APPDATA")
    file = open(appdata + '/Natural_Selection/Sprites/install.txt', "wb")
    print("Write file")
    file.write(base64.urlsafe_b64encode("version 1.6.1".encode("utf-8")))
    print("Done")


