import curses
from constants import *
from arena import *

def pause(screen, r, c):
    
    screen.clear()
    arena(screen)


    message = "--FIX THE TERMINAL SIZE--"

    if len('Pause') < c < len(message):
        message = "Pause"

    if c < len(message):
        message = "P"

    screen.addstr(r // 2, c // 2 - len(message)//2, message)