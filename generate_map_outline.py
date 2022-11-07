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
        outline.append([x, y, r, g, b])

    with open('data/outline.json', 'w') as f:
        json.dump(outline, f, indent=2)