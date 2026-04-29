import curses
from time import sleep
from menu import * 
from arena import arena
#from game import *
from pause import *
from game import *

def main(screen):
    while True:
        screen.clear()
        
        height, width = screen.getmaxyx()

        if height < 36 or width < 72:
            pause(screen, height, width)
        else:  
            arena(screen)
            screen.refresh()
            setting = menu(screen)
            game(screen, setting)

        screen.refresh()
        key = screen.getch()
        if key == ord('q'):
            break

        sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
