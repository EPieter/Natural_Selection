from .imports import *

#
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
