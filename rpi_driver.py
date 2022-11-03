from matrix import Matrix
from load import *
import json


if __name__ == "__main__":
    
    stops = load_stops()
    stop_coordinates = load_stop_coords()
    colors = load_colors()
    text = load_text()

    for _, stop in stops.items():
        try:
            x, y = stop_coordinates[stop['name']]
        except KeyError:
            continue
        for border in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            text.append(border)


    matrix = Matrix(default=text)

    try:
        while True:
            vehicles = load_vehicles()

            set_pixels = set()
            
            for vehicle, vehicle_info in vehicles.items():
                stop = vehicle_info['stop']
                if stop is not None:
                    try:
                        x, y = stop_coordinates[stops[stop]['name']]
                    except KeyError:
                        continue
                    if vehicle_info['current_status'] in ['IN_TRANSIT_TO', 'INCOMING_AT']:
                        flash = True
                    else:
                        flash = False
                    if (x, y) in set_pixels:
                        flash = not flash
                    color = colors[stops[stop]['line']]
                    matrix.set_pixel(x, y, color[0], color[1], color[2], flash=flash)
                    set_pixels.add((x, y))

            matrix.run_cycle()
    except KeyboardInterrupt:
        pass


