import time
import requests
import os
import base64
import tools

sprites = [
    "Big Factory.png",
    "Big House.png",
    "Bitcoin.png",
    "Clovers 00 seamless.jpg",
    "Diamond.png",
    "Medium House.png",
    "Small Factory.png",
    "Small House.png",
]
appdata = os.getenv("APPDATA")


def install():
    print("Installing...")
    print("Making dirs...")
    makeDirs()
    print("Load files...")
    loadSprites()
    print("Resizing images...")
    tools.resizeImageArray([36, 72])
    print("Append shortcut to Menu Start...")
    addToStartMenu()
    print("Successfully installed.")
    time.sleep(3)


def loadSprites():
    path = appdata + "/Natural_Selection/Sprites/normal/"
    url = 'http://nsgame.nl/Sprites/'
    for sprite in sprites:
        r = requests.get(url + sprite, allow_redirects=True)
        open(path + sprite, 'wb').write(r.content)
    r = requests.get(url + "OpenSans-SemiBold.ttf", allow_redirects=True)
    open(appdata + "/Natural_Selection/Sprites/OpenSans-SemiBold.ttf", "wb").write(r.content)
    r = requests.get(url + "icon.ico", allow_redirects=True)
    open(appdata + "/Natural_Selection/Sprites/icon.ico", "wb").write(r.content)
    r = requests.get(url + "Natural Selection.exe", allow_redirects=True)
    open(appdata + "/Natural_Selection/Natural Selection.exe", "wb").write(r.content)


def makeDirs():
    if not os.path.isdir(appdata + "/Natural_Selection"):
        os.mkdir(appdata + "/Natural_Selection")
    if not os.path.isdir(appdata + "/Natural_Selection/Sprites"):
        os.mkdir(appdata + "/Natural_Selection/Sprites")
    if not os.path.isdir(appdata + "/Natural_Selection/Sprites/normal"):
        os.mkdir(appdata + "/Natural_Selection/Sprites/normal")
    file = open(appdata + '/Natural_Selection/Sprites/install.txt', "wb")
    file.write(base64.urlsafe_b64encode("version 1.7.beta2".encode("utf-8")))


def addToStartMenu():
    import win32com.client
    path = appdata + r'\Microsoft\Windows\Start Menu\Programs\Natural Selection.lnk'
    target = appdata + "/Natural_Selection/Natural Selection.exe"
    icon = appdata + "/Natural_Selection/Sprites/icon.ico"
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()


if not os.path.exists(appdata + "/Natural_Selection/Sprites/install.txt"):
    install()
else:
    file1 = open(appdata + "/Natural_Selection/Sprites/install.txt", "rb")
    file_content = str(base64.urlsafe_b64decode(file1.read()), "utf-8")
    if not file_content == "version 1.7.beta2":
        import update
        update.Update()
    else:
        print("already satisfied")

