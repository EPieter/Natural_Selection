import os  # for handling files and directories
import requests  # for post request to the server


def check_user(username, password):
    if os.path.exists('../userdata.txt'):
        f = open('../userdata.txt')
        file_data = f.read()
        file_data = file_data.split("|")
        user = file_data[0]
        user_pass = file_data[1]
        url = 'http://nsgame.nl/app/conn.php'
        url_data_before_sending = {'method': 'get_user_data', 'user': user, 'password': user_pass}
        x = requests.post(url, data=url_data_before_sending)

    else:
        f = open('../userdata.txt', 'w')
        f.write(username+"|"+password)
        url = 'http://nsgame.nl/app/conn.php'
        url_data_before_sending = {'method': 'create_new_user', 'user': username, 'password': password}
        x = requests.post(url, data=url_data_before_sending)
        # TODO: else in this function

    return x.text