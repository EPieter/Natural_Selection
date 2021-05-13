import data
import requests as get
import os
import base64


class UserInformation:
    def __init__(self, location=None):
        if location is None:
            location = [data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_WIDTH, data.MIDDLE_OF_THE_SCREEN_IN_GRIDS_HEIGHT]
        self.last_location = location
        self.user_id = None
        self.user_name = None
        self.user_password = None
        self.user_play_level = None
        self.data_from_server = None
        self.information_to_send = None

    def get_variables(self):
        return self

    def check_user_information_file(self):
        if os.path.exists('/userdata.txt'):
            f = open('userdata.txt')
            file_data = f.read()
            if file_data != "":
                decoded_file_data = base64.b64encode(bytes(file_data, 'utf-8'))
                list_decoded_file_data = list(str(decoded_file_data))
                self.user_id = list_decoded_file_data[0]
                self.user_name = list_decoded_file_data[1]
                self.user_play_level = list_decoded_file_data[2]

    def create_user_information(self):
        user_name = self.user_name
        user_id = self.user_id
        user_password = self.user_password
        user_level = self.user_play_level
        user_information = [user_id, user_name, user_level]

    def send_info_to_cloud(self, info):
        info_to_send = info
        url = 'http://nsgame.nl/app/conn.php'
        x = get.post(url, info_to_send)
        self.data_from_server = x

    def save_information(self):
        self.information_to_send = self.test_information()
        self.send_info_to_cloud(self.information_to_send)

    def test_information(self):
        return {'location': self.last_location}

    def get_information(self):
        info = {'method': 'get', 'get': 'location'}
        self.send_info_to_cloud(info)

    def run_test(self):
        self.save_information()
        return self.data_from_server

# from files.controllers.connect_to_cloud.py
# # TODO: needs to run automatically when you start the game
# def check_user():
#     if os.path.exists('../userdata.txt'):
#         f = open('../userdata.txt')
#         file_data = f.read()
#         file_data = file_data.split("|")
#         user = file_data[0]
#         user_pass = file_data[1]
#         url = 'http://nsgame.nl/app/conn.php'
#         url_data_before_sending = {'method': 'get_user_data', 'user': user, 'password': user_pass}
#         x = get.post(url, data=url_data_before_sending)
#
#     else:
#         username = input("username: ")
#         password = input("password: ")
#         file_data_user_do_not_exist(username, password)
#
#     return x.text
#
#
# def file_data_user_do_not_exist(username, password):
#     f = open('../userdata.txt', 'w')
#     f.write(username + "|" + password)
#     url = 'http://nsgame.nl/app/conn.php'
#     url_data_before_sending = {'method': 'check_if_user_exist', 'user': username, 'password': password}
#     x = get.post(url, data=url_data_before_sending)
#     # TODO: ask for creating new user
