from constants import *
import random
import curses

def gen_food(snake):
    while True:
        pos = (random.randint(1, HEIGHT-2), random.randint(2, WIDTH-3))
        if pos not in snake:
            return pos

def change_direction(key, direction):
    if key == ord('w') and direction != (1, 0):
        return (-1, 0)
    elif key == ord('s') and direction != (-1, 0):
        return (1, 0)
    elif key == ord('a') and direction != (0, 1):
        return (0, -1)
    elif key == ord('d') and direction != (0, -1):
        return (0, 1)
    return direction

def is_collision(head, snake):

    r, c = head
    if r == 0 or r == HEIGHT - 1 or c == 1 or c == WIDTH - 2:
        return True

    if head in snake:
        return True

    return False

def draw_snake(screen, snake):
    for r, c in snake:
        try:
            screen.addstr(r, c, "@")
        except curses.error:
            pass

def draw_food(screen, food):
    r, c = food
    screen.addstr(r, c, "*")