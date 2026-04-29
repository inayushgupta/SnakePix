from constants import *
import random
import curses
from collections import deque

def move_snake(snake, direction, grow):
    
    r, c = snake[0]
    new_head = (r + direction[0], c + direction[1])
    snake.appendleft(new_head)

    if not grow:
        snake.pop()

def gen_food(snake):
    while True:
        pos = (random.randint(1, HEIGHT-2), random.randint(2, WIDTH-3))
        if pos not in snake:
            return pos

def change_direction(key, direction):
    if key in (UP, curses.KEY_UP) and direction != (1, 0):
        return (-1, 0)
    elif key in (DOWN, curses.KEY_DOWN) and direction != (-1, 0):
        return (1, 0)
    elif key in (LEFT, curses.KEY_LEFT) and direction != (0, 1):
        return (0, -1)
    elif key in (RIGHT, curses.KEY_RIGHT) and direction != (0, -1):
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