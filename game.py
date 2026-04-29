import curses
from arena import arena
import constants
from utils import *
from collections import deque
from time import sleep



def game(screen, setting):
    if setting is None:
        return

    screen.nodelay(True)
    screen.keypad(True)
    try:
        snake = deque([(12, 12), (12, 11), (12, 10)])
        direction = (0, 1)
        food = gen_food(snake)

        while True:
            screen.clear()

            arena(screen)
            draw_snake(screen, snake)
            draw_food(screen, food)

            new_head = (snake[0][0] + direction[0], 
                        snake[0][1] + direction[1])

            if is_collision(new_head, snake):
                screen.clear()
                break

            grow = new_head == food
            move_snake(snake, direction, grow)

            if grow:
                food = gen_food(snake)

            screen.refresh()

            key = screen.getch()
            direction = change_direction(key, direction)

            sleep(setting)
    finally:
        screen.nodelay(False)
        screen.keypad(False)

    




        
