import os  # for handling files and directories
import requests  # for post request to the server


def check_user(username, password):
    if os.path.exists('../userdata.txt'):
        f = open('../userdata.txt')
        file_data = f.read()
        file_data = file_data.split("|")
        user = file_data[0]
        passw = file_data[1]
        url = 'http://nsgame.nl/app/conn.php'
        url_data_before_sending = {'get_user_data': 'True', 'user': user, 'password': passw}
        x = requests.post(url, data=url_data_before_sending)

    else:
        f = open('../userdata.txt', 'w')
        f.write(username+"|"+password)
        url = 'http://nsgame.nl/app/conn.php'
        url_data_before_sending = {'user': username}
        # TODO: else in this function

    url = 'http://nsgame.nl/app/conn.php'
    url_data_before_sending = {'user': 'connected'}

    x = requests.post(url, data=url_data_before_sending)

    return x.text
