# 2048 Game in Python

A simple implementation of the popular 2048 game in Python. The objective of the game is to combine numbered tiles on a grid to create a tile with the number 2048.

## Game Rules
1. The game starts with a 4x4 grid filled with zeros.
2. Two random tiles (2 or 4) are added to the grid at the start.
3. Players can move the tiles in four directions: up, down, left, or right.
4. When two tiles with the same number touch, they merge into one.
5. The game continues until the player creates a tile with the number 2048 or there are no valid moves left.

## Features
- Move tiles using the keyboard (W, A, S, D).
- Clear console output for better visibility.
- Displays the current state of the game after each move.
- Checks for win/loss conditions.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository or download the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using the command:
   ```bash
   python 2048_game.py
