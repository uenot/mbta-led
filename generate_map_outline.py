from load import *
import json

if __name__ == "__main__":
    stops = load_stops()
    coords = load_stop_coords()
    colors = load_colors()

    outline = []
    for stop in stops.values():
        name = stop['name']
        x, y = coords[name]
        r, g, b = colors[stop['line']]
        outline_coords = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
        for x_o, y_o in outline_coords:
            outline.append([x_o, y_o, r, g, b])

    with open('data/outline.json', 'w') as f:
        json.dump(outline, f, indent=2)