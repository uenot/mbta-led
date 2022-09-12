from matrix import Matrix
from matrix_mapper_info import *
from load_stops import load_stops
from load_routes import load_routes
from load_vehicles import load_vehicles
import json
import time


if __name__ == "__main__":
    
    load_stops()
    load_routes()

    matrix = Matrix()

    with open('data/stops.json') as f:
        stops = json.load(f)

    try:
        while True:
            vehicles = load_vehicles(void=False)
            
            for vehicle, vehicle_info in vehicles.items():
                stop = vehicle_info['stop']
                if stop is not None:
                    try:
                        info = stop_coordinates[int(stop)]
                    except:
                        continue
                    if vehicle_info['current_status'] in ['IN_TRANSIT_TO', 'INCOMING_AT']:
                        flash = True
                    else:
                        flash = False
                    matrix.set_pixel(info[0], info[1], colors[info[2]][0], colors[info[2]][1], colors[info[2]][2], flash=flash)

            matrix.run_cycle()
    except KeyboardInterrupt:
        pass


