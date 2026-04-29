import curses
from time import sleep
from menu import * 
from arena import *

def main(screen):
    while True:
        screen.clear()
        
        height, width = screen.getmaxyx()

        if height < 36 or width < 72:
            screen.clear()
            screen.addstr(0, 0,  "Paused! Pease Fix the screen")
        else:
            arena(screen)
            screen.refresh()
            settings = menu(screen)
        screen.refresh()
        key = screen.getch()
        if key == ord('q'):
            break

        sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
