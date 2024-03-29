from load import *
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
    # initialize stdscr
    curses.start_color()
    stdscr.clear()
    try:
        while True:  # main control loop
            base_map = create_map()  # create map (based on vehicle locations)
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
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    wrapper(main)