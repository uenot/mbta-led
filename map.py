import json
import re


def create_map():
    with open('map.txt') as f:
        mbta_map = f.read()

    with open('data/vehicles.json') as f:
        vehicles = json.load(f)

    with open('data/stops.json') as f:
        stops = json.load(f)

    for vehicle, vehicle_info in vehicles.items():
        stop = vehicle_info['stop']
        if stop is not None:
            replace_str = f'{vehicle_info["route"][0].upper()} '
            if vehicle_info['current_status'] in ['IN_TRANSIT_TO', 'INCOMING_AT']:
                replace_str = 'f' + replace_str
            replace_str = ' ' + replace_str
            mbta_map = re.sub(f'( |\||[0-9])*{stop}( |\||[0-9])*', replace_str, mbta_map)
    for stop, stop_info in stops.items():
        mbta_map = re.sub(f'( |\||[0-9])*{stop}( |\||[0-9])*',
                          f' {stop_info["description"].split(" - ")[1][0].lower()} ',
                          mbta_map)
    mbta_map = re.sub('( )([A-Za-z]*)( / )([A-Za-z]*)( )', r"\2/\4", mbta_map)

    return mbta_map

def match_lower(match):
    return match.group(1).lower()

def match_upper(match):
    return match.group(1).upper()

def flicker_map(mbta_map, state):
    if state:
        return re.sub('f([A-Z])', match_upper, mbta_map)
    else:
        return re.sub('f([A-Z])', match_lower, mbta_map)

if __name__ == "__main__":
    mbta_map = create_map()
    print(mbta_map)
    print()
    flicker_1 = flicker_map(mbta_map, True)
    print(flicker_1)
    print()
    flicker_2 = flicker_map(mbta_map, False)
    print(flicker_2)
