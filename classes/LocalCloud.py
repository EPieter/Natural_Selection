import os
import sys
import data
from classes import Game


class LocalCloud:
    def __init__(self):
        self.location_from_file = None
        self.player_level = None
        self.buildings = []
        self.list_file_content = []
        self.standard_data = str(data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH)+"|"+str(data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT)+"|1|0:0:0;1:-1:0"
        self.standard_data_without_location = "|1|0:0:0;1:-1:0"

    def getAllData(self):
        dir_set = os.path.isdir("data")
        if dir_set:
            try:
                file = open("data/userdata.txt", "r")
            except IOError:
                file = open("data/userdata.txt", "w")
                file.write(self.standard_data)
                file = open("data/userdata.txt", "r")
        else:
            os.mkdir('data')
            os.system("attrib +h data")
            file = open('data/userdata.txt', "w")
            file.write(self.standard_data)
            file = open("data/userdata.txt", "r")
        file_content = file.read()
        file.close()
        self.list_file_content = file_content.split("|")
        Game.location = [int(self.list_file_content[0]), int(self.list_file_content[1])]

    def getBuildingsData(self):
        buildings_data = self.list_file_content[3]
        buildings_data = buildings_data.split(";")
        for data_ in buildings_data:
            new_data = data_.split(":")
        return buildings_data

    def updateUserData(self):
        file = open("data/userdata.txt", "w")
        file.write(str(Game.Game().location_x) + "|" + str(Game.Game().location_y) + self.standard_data_without_location)
