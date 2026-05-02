import curses
from arena import arena
import constants
from utils import *
from collections import deque
from time import sleep
from pause import *


def game(screen, setting):
    if setting is None:
        return
    
    score = 0
    screen.nodelay(True)
    screen.keypad(True)
    try:
        snake = deque([(12, 12), (12, 11), (12, 10)])
        direction = (0, 1)
        food = gen_food(snake)

        while True:
            r, c = screen.getmaxyx()

            if r < 36 or c < 72:
                pause(screen, r, c)
                screen.refresh()
                sleep(0.1)
                continue

            key = screen.getch()
            direction = change_direction(key, direction)

            new_head = (snake[0][0] + direction[0], 
                        snake[0][1] + direction[1])

            if is_collision(new_head, snake):
                screen.clear()
                break

            screen.clear()

            arena(screen)
            draw_snake(screen, snake)
            draw_food(screen, food)

            grow = new_head == food
            move_snake(snake, direction, grow)

            if grow:
                score += 1
                food = gen_food(snake)

            screen.refresh()

            sleep(setting)
    finally:
        screen.nodelay(False)
        screen.keypad(False)
        return score

    




        
