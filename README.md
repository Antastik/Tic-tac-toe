# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game written in Python.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)

## Overview

This is a text-based implementation of Tic-Tac-Toe where two players take turns marking spaces on a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features

- Interactive command-line interface
- Two-player gameplay (X and O)
- Move validation to prevent illegal moves
- Undo functionality to revert the last move
- Game statistics tracking (wins, losses, draws)
- Option to reset the game or quit at any time
- Clear visual representation of the game board

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone this repository or download the source files:
3. No additional dependencies are required!

## How to Play

1. Run the game using Python:
   ```
   python main.py
   ```

2. The game will display an empty 3×3 grid and prompt the first player (X) to make a move.

3. Enter your move by specifying the row and column numbers (0-2), separated by a space:
   ```
   Enter move (row col), 'undo', 'reset', 'stats', or 'quit': 1 1
   ```
   This would place your mark in the center of the board.

4. Players alternate turns until one player wins by getting three marks in a row (horizontally, vertically, or diagonally) or the game ends in a draw.

5. Special commands:
   - `undo`: Reverts the last move
   - `reset`: Starts a new game
   - `stats`: Displays player statistics
   - `quit`: Exits the game

## Code Structure

The game is organized into four Python files:

### main.py
The entry point of the application. Handles user input, game flow, and displays the game state.

### game.py
Contains the `Game` class which manages the game state, player turns, and win conditions.

### board.py
Implements the `Board` class that represents the game board, tracks moves, and checks for winning conditions.

### player.py
Defines the `Player` class that stores player information and statistics.

## Future Improvements

- Add an AI opponent with adjustable difficulty levels
- Implement a graphical user interface (GUI)
- Add network play functionality for remote games
- Save game statistics between sessions
- Add replay functionality to review past games