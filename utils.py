from constants import *
import random
import curses
from collections import deque

def move_snake(snake, direction, grow):
    
    r, c = snake[0]
    new_head = (r + direction[0], c + direction[1])
    snake.appendleft(new_head)

def gen_food(snake):
    while True:
        pos = (random.randint(3, HEIGHT-2), random.randint(2, WIDTH-2))
        if not snake.is_part_of(pos):
            return pos

def draw_food(screen, food):
    r, c = food
    screen.addstr(r, c, "*")