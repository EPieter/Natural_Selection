import os
import data
import json


class LocalCloud:
    def __init__(self):
        self.location_from_file = None
        self.player_level = None
        self.buildings = []
        self.list_file_content = []
        self.standard_data = json.dumps({
            'location': [data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH, data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT],
            'people': 15,
            'money': 1000,
            'buildings': [
                [14, 8, 0],
                [14, 9, 0],
                [13, 8, 0],
                [15, 8, 0],
                [14, 7, 0],
            ],
        })
        self.userdata = {
            'location': [0, 0],
        }

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
        file.close()
        self.getUserData()
        return self.userdata

    def updateUserData(self, game):
        self.userdata['location'] = [game.location_x, game.location_y]
        self.userdata['buildings'] = game.buildings
        self.userdata['money'] = game.money
        self.userdata['people'] = game.people_in_the_city
        file = open("data/userdata.txt", "w")
        json_userdata = json.dumps(self.userdata)
        file.write(json_userdata)

    def getUserData(self):
        file = open("data/userdata.txt", "r")
        file_content = file.read()
        file_content = json.loads(file_content)
        self.userdata = file_content
