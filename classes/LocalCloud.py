import os
import data
import json
import base64


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
                [15, 9, 0],
                [15, 10, 0],
                [14, 9, 0],
                [16, 9, 0],
                [15, 8, 0],
            ],
            'dark_mode': False
        })
        self.userdata = {
            'location': [0, 0],
        }
        self.appdata_path = os.getenv("APPDATA")

    def getAllData(self):
        dir_set = os.path.isdir(self.appdata_path + "/Natural_Selection/data")
        if dir_set:
            try:
                file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "rb")
            except IOError:
                file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "wb")
                json_userdata = self.standard_data
                encoded_userdata = base64.urlsafe_b64encode(json_userdata.encode("utf-8"))
                file.write(encoded_userdata)
                file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "rb")
        else:
            os.mkdir(self.appdata_path + "/Natural_Selection/data")
            file = open(self.appdata_path + '/Natural_Selection/data/userdata.jpg', "wb")
            json_userdata = self.standard_data
            encoded_userdata = base64.urlsafe_b64encode(json_userdata.encode("utf-8"))
            file.write(encoded_userdata)
            file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "rb")
        file.close()
        self.getUserData()
        return self.userdata

    def updateUserData(self, game):
        self.userdata['location'] = [game.location_x, game.location_y]
        self.userdata['buildings'] = game.buildings
        self.userdata['money'] = game.money
        self.userdata['people'] = game.people_in_the_city
        self.userdata['dark_mode'] = game.dark_mode
        file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "wb")
        json_userdata = json.dumps(self.userdata)
        encoded_userdata = base64.urlsafe_b64encode(json_userdata.encode("utf-8"))
        file.write(encoded_userdata)

    def getUserData(self):
        file = open(self.appdata_path + "/Natural_Selection/data/userdata.jpg", "rb")
        file_content = file.read()
        decoded_userdata = base64.urlsafe_b64decode(file_content)
        file_content = json.loads(decoded_userdata)

        self.userdata = file_content

        if 'dark_mode' not in self.userdata:
            self.userdata["dark_mode"] = False
        if 'lang' not in self.userdata:
            self.userdata['lang'] = 'nl'

