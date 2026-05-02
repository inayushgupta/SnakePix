# SnakePix

SnakePix is a stable terminal-based clone of the classic Snake game built with Python and `curses`.

## Description

A simple, polished Snake game for terminal environments. The game includes a difficulty menu, fixed board layout, and responsive controls for a consistent ASCII-style play experience.

## Features

- Fixed board size: `72 x 36`
- `WASD` and arrow key movement
- Difficulty selection menu
- Food spawns inside the board walls
- Walls are rendered using `0` characters
- Clean separation of game logic, rendering, and utilities

## Requirements

- Python 3.13+
- Terminal with `curses` support
- `uv` is optional but recommended for running the app

## Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade pip:
   ```bash
   python -m pip install --upgrade pip
   ```

## Running the Game

From the project root:

- Recommended (if `uv` is installed):
  ```bash
  uv run main.py
  ```

- Fallback option:
  ```bash
  python main.py
  ```

## Controls

- `W` or `Up Arrow`: move up
- `S` or `Down Arrow`: move down
- `A` or `Left Arrow`: move left
- `D` or `Right Arrow`: move right
- `Q`: quit from the main screen

## Project Structure

- `main.py` — game entry point and main loop
- `menu.py` — difficulty selection menu
- `game.py` — core game logic, movement, collision, and food handling
- `arena.py` — board rendering and wall layout
- `utils.py` — helper functions for movement, collision, and food generation
- `pause.py` — pause/resize handling when terminal is too small
- `constants.py` — fixed board dimensions and input key constants

## Notes

- The game uses a fixed board size, so the terminal must be at least `72` columns by `36` rows.
- No external dependencies are required beyond Python and `curses`.