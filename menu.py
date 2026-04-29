import curses
from constants import *
from arena import *

def menu(screen):
    
    menu_options = ['EASY', 'MEDIUM', 'HARD']
    settings = {key:value for key, value in enumerate(menu_options)}
    heading = "SNAKE PIX!"
    selection = 0

    while True:
        screen.clear()
        height, width = screen.getmaxyx()
        arena(screen)
        try:

            if height < 36 or width < 72:
                raise curses.error

            screen.addstr(HEIGHT//3 - 6, (WIDTH // 2) - len(heading)//2  , heading)        
            screen.addstr(HEIGHT//3 + 6 + selection * 2, (WIDTH // 2) - 10, ">>")
            for i, option in enumerate(menu_options):
                screen.addstr(HEIGHT//3 + 6 + i * 2, (WIDTH // 2) - len(option)//2, option)

            screen.refresh() 
        except curses.error:
            return
        key = screen.getch()

        if key == ord('s'):
            selection = selection + 1 if selection < 2 else selection
        elif key == ord('w'):
            selection = selection - 1 if selection > 0 else selection
        elif key == ord('\n'):
            return settings[selection]


