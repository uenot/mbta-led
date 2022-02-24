import requests
import json
import os
import config

response = requests.get(f'https://api-v3.mbta.com/routes?api_key={config.key}&filter[type]=0,1')
data = response.json()['data']
formatted = {}
for route in data:
    keys = ['direction_destinations', 'color', 'long_name']
    print(route)
    formatted[route['id']] = {k: route['attributes'][k] for k in keys}
if not os.path.exists('data'):
    os.makedirs('data')
with open('data/routes.json', 'w') as f:
    json.dump(formatted, f, indent=2)


