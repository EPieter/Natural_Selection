import requests  # for get info from cloud
import data  # for useful info in our project


class Cloud:
    def __init__(self):
        self.connected_with_cloud = False
        self.tryToConnectWithCloud()

    def tryToConnectWithCloud(self):
        data_to_send = {'try_to_connect': 'give_return'}
        try:
            x = requests.post(data.app_url + "test_connection", data_to_send)
        except:
            self.connected_with_cloud = False
            return 0
        if x.text == "connected":
            self.connected_with_cloud = True


