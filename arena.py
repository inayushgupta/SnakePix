import curses

def arena(screen):
    height, width = screen.getmaxyx()

    if height < 36 or width < 72:
        text = "Paused! Please fix the screen"
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
