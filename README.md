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

## Known issues and suggested fixes

1. `utils.is_collision()` has an incorrect right-wall boundary check.
   - The board draws walls at `c == 70` and `c == 71`, but collision only checks `c == WIDTH - 1`.
   - Fix: treat `c == WIDTH - 2` and `c == WIDTH - 1` as collisions.

2. Moving into the tail should be allowed when the snake is not growing.
   - Current collision detection checks the entire snake body before the tail is removed.
   - Fix: allow the new head to occupy the current tail cell on non-growth moves.

3. `constants.py` defines `LEFT` and `RIGHT` opposite of the expected WASD mapping.
   - `LEFT = ord('d')` and `RIGHT = ord('a')` are reversed.
   - Fix: swap them so `A` is left and `D` is right.

4. `menu.py` only uses `w`/`s` for selection, not arrow key input.
   - Adding arrow key support would improve usability.

5. `draw_food()` does not catch `curses.error`.
   - If food spawns outside the visible region or if the terminal is too small, the game may crash.
   - Fix: wrap drawing in a `try/except curses.error` block.

6. The fixed-board logic is built around a `36x72` viewport.
   - If the user resizes the terminal, the game currently may not behave consistently.
   - Consider enforcing the fixed size more strictly or using the actual terminal dimensions uniformly.

## Notes

- The game intentionally uses a fixed board size, so the terminal must be at least `72` columns by `36` rows.
- If the terminal is too small, the app shows a resize warning and returns to the main menu.
