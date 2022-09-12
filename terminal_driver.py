from load_stops import *
from load_routes import *
from load_vehicles import *
from map import *
import time
import curses
from curses import wrapper


def main(stdscr):
    """
    Loads the MBTA data and displays that data in a terminal window.
    Passed as an argument into the curses wrapper function.
    :param stdscr: A window object representing the screen; passed in by wrapper.
    """
    # load initial data (doesn't change over time)
    load_stops()
    load_routes()
    # initialize stdscr
    curses.start_color()
    stdscr.clear()
    while True:  # main control loop
        load_vehicles()  # get vehicle locations (needs to be in realtime)
        base_map = create_map()  # create map (based on those vehicle locations)
        flicker_state = True
        # initialize colors
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        colors = {
            'g': 1,
            'r': 2,
            'm': 2,
            'o': 3,
            'b': 4
        }
        for _ in range(6):
            stdscr.clear()
            flickered_map = flicker_map(base_map, flicker_state)
            for char in flickered_map:
                stdscr.addstr(char, curses.color_pair(colors.get(char.lower(), 0)))
            stdscr.refresh()
            time.sleep(1)
            flicker_state = not flicker_state


wrapper(main)
