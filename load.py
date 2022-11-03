import requests
import config
import json

def load_stops():
    response = requests.get(f'https://api-v3.mbta.com/stops?api_key={config.key}&filter[route_type]=0,1')
    data = response.json()['data']
    formatted = {}
    for stop in data:
        keys = ['name', 'platform_name', 'description']
        stop_data = {k: stop['attributes'][k] for k in keys}
        stop_data['line'] = stop_data['description'].split(' - ')[1].split(' ')[0]
        formatted[stop['id']] = stop_data

    return formatted

def load_vehicles():
    response = requests.get(f"https://api-v3.mbta.com/vehicles?api_key={config.key}&filter[route_type]=0,1")
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
    return formatted

def load_stop_coords():
    with open('data/stops.json') as f:
        return json.load(f)

def load_colors():
    with open('data/colors.json') as f:
        return json.load(f)

def load_text():
    with open('data/text.json') as f:
        return json.load(f)