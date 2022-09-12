from matrix import Matrix
from matrix_mapper_info import *
from load_stops import load_stops
from load_vehicles import load_vehicles
import json
import time


if __name__ == "__main__":
    matrix = Matrix()

    load_stops()

    with open('data/stops.json') as f:
        stops = json.load(f)

    while True:
        load_vehicles()
        with open('data/vehicles.json') as f:
            vehicles = json.load(f)
        
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


