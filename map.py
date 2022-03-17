import json
import re

with open('map.txt') as f:
    mbta_map = f.read()

with open('data/vehicles.json') as f:
    vehicles = json.load(f)

with open('data/stops.json') as f:
    stops = json.load(f)

for vehicle, vehicle_info in vehicles.items():
    stop = vehicle_info['stop']
    if stop is not None:
        mbta_map = re.sub(f'( |\||[0-9])*{stop}( |\||[0-9])*', f' {vehicle_info["route"][0].upper()} ', mbta_map)
for stop, stop_info in stops.items():
    mbta_map = re.sub(f'( |\||[0-9])*{stop}( |\||[0-9])*',
                      f' {stop_info["description"].split(" - ")[1][0].lower()} ',
                      mbta_map)
mbta_map = re.sub('( )([A-Za-z])( / )([A-Za-z])( )', r"\2/\4", mbta_map)

print(mbta_map)