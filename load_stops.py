import requests
import json
import os
import config


def load_stops():
    response = requests.get(f'https://api-v3.mbta.com/stops?api_key={config.key}&filter[route_type]=0,1')
    data = response.json()['data']
    formatted = {}
    for stop in data:
        keys = ['name', 'platform_name', 'description']
        stop_data = {k: stop['attributes'][k] for k in keys}
        stop_data['line'] = stop_data['description'].split(' - ')[1].split(' ')[0]
        formatted[stop['id']] = stop_data

    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/stops.json', 'w') as f:
        json.dump(formatted, f, indent=2)


if __name__ == "__main__":
    load_stops()
