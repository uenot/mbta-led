import requests
import json
import os
import config

# errors if file doesn't exist
with open('data/routes.json') as f:
    routes = json.load(f)

response = requests.get(f'https://api-v3.mbta.com/vehicles?api_key={config.key}&filter[route_type]=0,1')
data = response.json()['data']
formatted = {}
for vehicle in data:
    keys = ['current_status', 'direction_id']
    vehicle_data = {k: vehicle['attributes'][k] for k in keys}
    vehicle_data['route'] = vehicle['relationships']['route']['data']['id']
    try:
        vehicle_data['stop'] = vehicle['relationships']['stop']['data']['id']
    except TypeError:
        vehicle_data['stop'] = None
    formatted[vehicle['id']] = vehicle_data

if not os.path.exists('data'):
    os.makedirs('data')
with open('data/vehicles.json', 'w') as f:
    json.dump(formatted, f, indent=2)
