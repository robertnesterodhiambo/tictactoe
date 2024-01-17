# Tic Tac Toe Game

## Overview

This is a simple console-based Tic Tac Toe game implemented in Python. The game allows two players to take turns marking spaces on a 3x3 grid, and the first player to get three marks in a row (horizontally, vertically, or diagonally) wins the game.

## Features

- **Two-player Gameplay:** The game is designed for two players to take turns playing.
- **Interactive Console Interface:** Users interact with the game through the console, inputting their moves.
- **Winning Logic:** The game automatically checks for a winning condition after each move to determine if a player has won.
- **Error Handling:** Proper error handling is implemented to handle invalid inputs and prevent crashes.

 welcome 
## How to Play

1. **Run the Game:**
   - Ensure you have Python installed on your machine.
   - Run the `tictactoe.py` script in your terminal or command prompt.

2. **Player Input:**
   - Players are prompted to input their moves by entering the row and column numbers of the grid.

3. **Winning the Game:**
   - The game ends when one player gets three marks in a row or when the grid is full, resulting in a draw.

4. **Restart:**
   - Players have the option to restart the game after it concludes.

## Requirements

- Python 3.x

## Usage

```bash
python tictactoe.py


Welcome to Tic Tac Toe!

Player 1 (X) - Enter your move (row and column): 1 1
   1 2 3
1  X |   |
  ---|---|---
2    |   |
  ---|---|---
3    |   |

Player 2 (O) - Enter your move (row and column): 2 2
   1 2 3
1  X |   |
  ---|---|---
2    | O |
  ---|---|---
3    |   |

...

Player 1 wins!
Do you want to play again? (yes/no): no

Thanks for playing!
