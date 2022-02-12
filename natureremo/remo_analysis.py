import requests
import json

IP_ADDRESS = '192.168.11.14'
FILE_NAME = 'output.json'

url = 'http://' + IP_ADDRESS + '/messages'
headers = {'X-Requested-With': 'local'}

res = requests.get(url, headers = headers)
data = json.loads(res.text)

file = open('./data/' + FILE_NAME, 'w')
print(json.dumps(data, indent=4), file=file)
file.close()