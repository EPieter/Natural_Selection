import requests  # for get info from cloud
import data  # for useful info in our project
import os


class Cloud:
    def __init__(self):
        self.connected_with_cloud = False
        self.tryToConnectWithCloud()
        if self.connected_with_cloud:
            print("Connection with server succeed")
        elif not self.connected_with_cloud:
            print("No connection with server")
        self.location = []

    def tryToConnectWithCloud(self):
        data_to_send = {'try_to_connect': 'give_return'}
        try:
            x = requests.post(data.app_url + "test_connection", data_to_send)
        except Exception as err:
            self.connected_with_cloud = False
            return err
        if x.text == "connected":
            self.connected_with_cloud = True

    def findOutIfCloudOrLocal(self):
        dir_set = os.path.isdir("data")
        if dir_set:
            try:
                file = open("data/userdata.txt", "r")
            except IOError:
                file = open("data/userdata.txt", "x")
        else:
            os.mkdir('data')
            os.system("attrib +h data")
            file = open("data/userdata.txt", "x")
        file_content = file.read()
        file.close()
        if file_content == "online":
            self.findLocationCloud()
        else:
            self.findLocationLocal()

    def findLocationCloud(self):
        pass

    def findLocationLocal(self):
        pass


