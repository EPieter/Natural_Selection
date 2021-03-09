from imports import *  # import all modules and files


def check_user():
    if os.path.exists('../userdata.txt'):
        f = open('../userdata.txt')
        file_data = f.read()
        file_data = file_data.split("|")
        user = file_data[0]
        password = file_data[1]
        url = 'http://nsgame.nl/app/conn.php'
        url_data_before_sending = {'user': user, 'password': password}
        x = requests.post(url, data=url_data_before_sending)

    else:
        x = True
        # TODO: else in this function

    url = 'http://nsgame.nl/app/conn.php'
    url_data_before_sending = {'user': 'connected'}

    x = requests.post(url, data=url_data_before_sending)

    return x.text
