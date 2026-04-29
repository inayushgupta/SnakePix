import curses
from time import sleep

def main(screen):
    while True:
        screen.clear()
        
        height, width = screen.getmaxyx()
        if height < 36 or width < 72:
            text = "Paused! Pease Fix the screen"
            screen.addstr(0, 0, text)
        else:
            try:            
                for r in range(36):
                    if r == 0 or r == 35:
                        for c in range(72):
                            screen.addstr(r, c, "0")
                        continue
    
                    for c in [0, 1, 70, 71]:
                        screen.addstr(r, c, "0")
            except curses.error:
                pass

        screen.refresh()
        key = screen.getch()
        if key == ord('q'):
            break

        sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
