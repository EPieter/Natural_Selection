import requests
import os
import base64
from classes import ExtraTools

version = "1.7.beta3"

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
    makeDirs()
    loadSprites()
    ExtraTools.resizeImageArray([36, 72])
    addToStartMenu()


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


def makeDirs():
    if not os.path.isdir(appdata + "/Natural_Selection"):
        os.mkdir(appdata + "/Natural_Selection")
    if not os.path.isdir(appdata + "/Natural_Selection/Sprites"):
        os.mkdir(appdata + "/Natural_Selection/Sprites")
    if not os.path.isdir(appdata + "/Natural_Selection/Sprites/normal"):
        os.mkdir(appdata + "/Natural_Selection/Sprites/normal")
    file = open(appdata + '/Natural_Selection/Sprites/install.txt', "wb")
    file.write(base64.urlsafe_b64encode(("version " + version).encode("utf-8")))


def addToStartMenu():
    import os
    import win32api
    import win32com.client

    path = r'C:/Users/' + win32api.GetUserName() + r'\AppData\Roaming\Microsoft\Windows\Start ' \
                                                   r'Menu\Programs\Natural ' \
                                                   r'Selection.lnk'

    target = os.getcwd() + "/NaturalSelection.v" + version + ".exe"
    icon = appdata + "/Natural_Selection/Sprites/icon.ico"
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()

