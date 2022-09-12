from rpi_driver import *
import json
import time

stop_coordinates = {
    70036: (39, 2, "orange"),
    70035: (39, 4, "orange"),
    70034: (39, 4, "orange"),
    70033: (39, 6, "orange"),
    70032: (39, 6, "orange"),
    70279: (39, 8, "orange"),
    70278: (39, 8, "orange"),
    70031: (39, 10, "orange"),
    70030: (39, 10, "orange"),
    70029: (39, 12, "orange"),
    70028: (39, 12, "orange"),
    70027: (39, 16, "orange"),
    70026: (39, 16, "orange"),
    70025: (39, 18, "orange"),
    70024: (39, 18, "orange"),
    70023: (39, 22, "orange"),
    70022: (39, 22, "orange"),
    70021: (37, 24, "orange"),
    70020: (37, 24, "orange"),
    70019: (35, 26, "orange"),
    70018: (35, 26, "orange"),
    70017: (33, 28, "orange"),
    70016: (33, 28, "orange"),
    70015: (31, 30, "orange"),
    70014: (31, 30, "orange"),
    70013: (29, 32, "orange"),
    70012: (29, 32, "orange"),
    70011: (27, 34, "orange"),
    70010: (27, 34, "orange"),
    70009: (25, 36, "orange"),
    70008: (25, 36, "orange"),
    70007: (23, 38, "orange"),
    70006: (23, 38, "orange"),
    70005: (21, 40, "orange"),
    70004: (21, 40, "orange"),
    70003: (19, 42, "orange"),
    70002: (19, 42, "orange"),
    70001: (17, 44, "orange"),
    70000: (17, 44, "orange"),

    70060: (55, 6, "blue"),
    70059: (55, 6, "blue"),
    70058: (53, 8, "blue"),
    70057: (53, 8, "blue"),
    70056: (51, 10, "blue"),
    70055: (51, 10, "blue"),
    70054: (49, 12, "blue"),
    70053: (49, 12, "blue"),
    70052: (47, 14, "blue"),
    70051: (47, 14, "blue"),
    70050: (45, 16, "blue"),
    70049: (45, 16, "blue"),
    70048: (43, 18, "blue"),
    70047: (43, 18, "blue"),
    70046: (41, 20, "blue"),
    70045: (41, 20, "blue"),
    70044: (39, 22, "blue"),
    70043: (39, 22, "blue"),
    70042: (37, 24, "blue"),
    70041: (37, 24, "blue"),
    70040: (35, 22, "blue"),
    70039: (35, 22, "blue"),
    70838: (33, 20, "blue"),
    70038: (33, 20, "blue")
}

colors = {
    "red": (255, 0, 0),
    "orange": (255, 215, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}

matrix = Matrix()

with open('data/vehicles.json') as f:
    vehicles = json.load(f)

with open('data/stops.json') as f:
    stops = json.load(f)

for vehicle, vehicle_info in vehicles.items():
    stop = vehicle_info['stop']
    if stop is not None:
        try:
            info = stop_coordinates[int(stop)]
        except:
            continue
	print(info)
        if vehicle_info['current_status'] in ['IN_TRANSIT_TO', 'INCOMING_AT']:
            flash = True
        else:
            flash = False
        matrix.set_pixel(info[0], info[1], colors[info[2]][0], colors[info[2]][1], colors[info[2]][2], flash=flash)

matrix.run_cycle()


