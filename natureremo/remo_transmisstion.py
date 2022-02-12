import requests
import json

IP_ADDRESS = '192.168.11.14'
FILE_NAME = 'output.json'

url = 'http://' + IP_ADDRESS + '/messages'
headers = {'X-Requested-With': 'local'}

file = open('./data/' + FILE_NAME, 'r')
data = file.read()
file.close()

res = requests.post(url, data=json.dumps(data), headers = headers)