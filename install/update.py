import os
import base64
import install
appdata = os.getenv("APPDATA")


def Update():
    print("Updating...")
    file = open(appdata + "/Natural_Selection/Sprites/install.txt", "rb")
    file_content = str(base64.urlsafe_b64decode(file.read()), "utf-8")
    version = file_content.split()[1]
    if version == "1.6.1" or "1.6" or "version 1.7.beta1":
        install.addToStartMenu()
    file = open(appdata + '/Natural_Selection/Sprites/install.txt', "wb")
    print("Write file")
    file.write(base64.urlsafe_b64encode("version 1.7.beta2".encode("utf-8")))
    print("Done")
