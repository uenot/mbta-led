from matrix import Matrix
from matrix_mapper_info import stop_coordinates, colors, text
from load import load_stops, load_vehicles
import json


if __name__ == "__main__":
    
    stops = load_stops()

    for _, stop in stops.items():
        try:
            x, y = stop_coordinates[stop['name']]
        except KeyError:
            continue
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                text.append((x+i, y+j))


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


