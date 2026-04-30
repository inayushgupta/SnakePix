# SnakePix

SnakePix is a terminal-based clone of the classic Snake game built with Python and `curses`.

## Overview

- Fixed board size: `72 x 36`
- Controls using `WASD` and arrow keys
- Simple menu for difficulty selection
- Food spawns inside the board walls
- Walls are rendered using `0` characters

## Requirements

- Python 3.13+
- A terminal that supports `curses`
- `uv` is optional but recommended for running the app

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   ```
3. Run the game:
   ```bash
   uv run main.py
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
- `game.py` — game logic, movement, collision, and food handling
- `arena.py` — renders the fixed board and wall layout
- `utils.py` — helper functions for movement, collisions, and food generation
- `pause.py` — pause screen when terminal is too small
- `constants.py` — fixed board dimensions and input key constants

## Notes

- The game intentionally uses a fixed board size, so the terminal must be at least `72` columns by `36` rows.