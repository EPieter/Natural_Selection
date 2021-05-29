import requests  # for get info from cloud
import data  # for useful info in our project


class Cloud:
    def __init__(self):
        self.connected_with_cloud = False
        self.tryToConnectWithCloud()
        if self.connected_with_cloud:
            print("Connection with server succeed")
        elif not self.connected_with_cloud:
            print("No connection with server")
        self.location = []
        self.findLocationCloud()
        self.findLocationLocal() if self.location == [] else None

    def tryToConnectWithCloud(self):
        data_to_send = {'try_to_connect': 'give_return'}
        try:
            x = requests.post(data.app_url + "test_connection", data_to_send)
        except Exception as err:
            self.connected_with_cloud = False
            return err
        if x.text == "connected":
            self.connected_with_cloud = True

    def findLocationCloud(self):
        pass

    def findLocationLocal(self):
        pass


