import requests
import json
import os
import config

# errors if file doesn't exist
with open('data/routes.json') as f:
    routes = json.load(f)


def load_stops():
    response = requests.get(f'https://api-v3.mbta.com/stops?api_key={config.key}&filter[route_type]=0,1')
    data = response.json()['data']
    formatted = {}
    for stop in data:
        keys = ['name', 'platform_name', 'description']
        formatted[stop['id']] = {k: stop['attributes'][k] for k in keys}

    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/stops.json', 'w') as f:
        json.dump(formatted, f, indent=2)


if __name__ == "__main__":
    load_stops()
