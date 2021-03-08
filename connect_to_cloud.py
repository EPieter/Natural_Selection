from imports import *  # import all modules and files

url = 'http://nsgame.nl/index.php'
data = {'test': 'connected'}

x = requests.post(url, data=data)

print(x.text)
