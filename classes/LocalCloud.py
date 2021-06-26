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
                file = open("data/userdata.jpg", "rb")
            except IOError:
                file = open("data/userdata.jpg", "wb")
                json_userdata = json.dumps(self.standard_data)
                encoded_userdata = base64.b64encode(json_userdata.encode("utf-8"))
                file.write(encoded_userdata)
                file = open("data/userdata.jpg", "rb")
        else:
            os.mkdir('data')
            os.system("attrib +h data")
            file = open('data/userdata.jpg', "wb")
            json_userdata = json.dumps(self.standard_data)
            encoded_userdata = base64.b64encode(json_userdata.encode("utf-8"))
            file.write(encoded_userdata)
            file = open("data/userdata.jpg", "rb")
        file.close()
        self.getUserData()
        return self.userdata

    def updateUserData(self, game):
        self.userdata = json.loads(self.userdata) if type(self.userdata) == "str" else self.userdata

        self.userdata['location'] = [game.location_x, game.location_y]
        self.userdata['buildings'] = game.buildings
        self.userdata['money'] = game.money
        self.userdata['people'] = game.people_in_the_city
        file = open("data/userdata.jpg", "wb")
        json_userdata = json.dumps(self.userdata)
        encoded_userdata = base64.b64encode(json_userdata.encode("utf-8"))
        file.write(encoded_userdata)

    def getUserData(self):
        file = open("data/userdata.jpg", "rb")
        file_content = file.read()
        decoded_userdata = base64.b64decode(file_content)
        file_content_decoded = json.loads(decoded_userdata)
        self.userdata = file_content_decoded
