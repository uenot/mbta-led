from load_stops import *
from load_routes import *
from load_vehicles import *
from map import *
import time
import curses
from curses import wrapper


def main(stdscr):
    load_stops()
    load_routes()
    curses.start_color()
    while True:
        stdscr.clear()
        load_vehicles()
        base_map = create_map()
        flicker_state = True
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
        for i in range(6):
            stdscr.clear()
            flickered_map = flicker_map(base_map, flicker_state)
            for char in flickered_map:
                stdscr.addstr(char, curses.color_pair(colors.get(char.lower(), 0)))
            stdscr.refresh()
            time.sleep(1)
            flicker_state = not flicker_state


wrapper(main)
