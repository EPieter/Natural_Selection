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
            'location': [data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH,
                         data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT],
            'level': 0,
            'resources': {'wood': 50, 'stone': 20, },
            'buildings': [
                [0, 1, [0, 0]],  # city hall
                [1, 1, [0, 1]],  # way
            ]
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
        return self.userdata['location']

    def updateUserData(self, location):
        self.userdata['location'] = location
        file = open("data/userdata.txt", "w")
        json_userdata = json.dumps(self.userdata)
        file.write(json_userdata)

    def getUserData(self):
        file = open("data/userdata.txt", "r")
        file_content = file.read()
        file_content = json.loads(file_content)
        self.userdata = file_content
