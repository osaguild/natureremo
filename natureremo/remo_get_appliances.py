import requests
import json

TOKEN = 'xxx'

url = 'https://api.nature.global/1/appliances'
headers = {'Authorization': 'Bearer ' + TOKEN}

res = requests.get(url, headers = headers)
appliances = json.loads(res.text)

print('Your appliances lists is ...')
for appliance in appliances:
    type = ''
    model = ''
    name = ''
    id = ''
    if appliance['type'] is not None:
        type = appliance['type']
    if appliance['model'] is not None:
        model = appliance['model']
        if model['name'] is not None:
            name = model['name']
    if appliance['id'] is not None:
        id = appliance['id']

    data = '{0:<10} | {1:<20} | {2}'.format(type,name,id)
    print(data)
