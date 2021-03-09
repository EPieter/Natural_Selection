from imports import *  # import all modules and files

url = 'http://nsgame.nl/app/conn.php'
data = {'test': 'connected'}

x = requests.post(url, data=data)

print(x.text)
