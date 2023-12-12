"""
This module contains the components of the Battleships game.

It includes functions to initialise the game board, create battleships from a file, 
and constants for the game directions. The board size can be specified when initialising 
the board, and the battleships are created from a text file which can also be specified.
The algorithm used to place the battleships can also be specified.
- simple: places the battleships on each row
- random: places the battleships randomly on the board
- custom: places the battleships using a custom algorithm

Constants:
    DOWN: Represents the direction down of a ship.
    RIGHT: Represents the direction right of a ship.

This module is used by the main server module to handle the core game logic.
"""

import os
import json
from random import randint


# Constants
DOWN = 0
RIGHT = 1


def initialise_board(size: int = 10) -> list[list[None]]:
    """Initialises and returns a board of size * size

    This function creates a square board with each cell set to None.
    The size of the board is specified by the 'size' argument. If argument is not provided,
    a default size of 10 is used. The function checks if the size is an integer and within
    the range of 5 to 10, inclusive. If not, it raises an appropriate error.


    Keyword arguments:
    size -- the size of the board (default 10, range: 5-10)
    """
    # Checks if size is an integer and within range
    if size < 5 or size > 10:
        raise ValueError("Size must be between 5 and 10")
    # Checks if size is an integer or None (defaults to 10)
    if not isinstance(size, int) or size is None:
        raise TypeError("Size must be an integer")
    # Creates a board of size * size
    board = [[None] * size for _ in range(size)]
    return board


def create_battleships(filename: str = "battleships.txt") -> dict[str, int]:
    """
    Reads the text file and returns battleships as a dictionary.

    The input file should be formatted as follows:
    Each line represents one battleship, with the name of the battleship
    and its size separated by a colon.
    For example:
        Carrier:5
        Battleship:4
        Cruiser:3
        Submarine:3
        Destroyer:2

    Keyword arguments:
    filename -- name of file containing battleship data (default "battleships.txt")
                must include file extension within argument.
    """
    battleships = {}
    # Checks if filename is a string or None (defaults to "battleships.txt")
    if not isinstance(filename, str) or filename is None:
        raise TypeError("Filename must be a string")
    try:
        # Gets and constructs absolute path of file
        # This is so that the file can be accessed by any environment
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        # Opens battleships.txt to read file
        with open(file_path, "r", encoding="utf-8") as f:
            # Reads each line of the file
            filelines = f.readlines()
            # Iterates through each line
            for line in filelines:
                # Splits and strips lines into ship name and length
                ship = line.strip().split(":")
                # Checks if ship is a valid list
                if len(ship) == 2:
                    # Adds ship to dictionary with name as key and length as value
                    battleships[ship[0]] = int(ship[1])
                else:
                    raise ValueError("Invalid data format in the file")
    # Raises and handles error if file is not found
    except FileNotFoundError as err:
        raise FileNotFoundError(f"File '{filename}' not found") from err
    return battleships


def is_position_occupied(
    board: list[list], col: int, row: int, direction: int, length: int
) -> bool:
    """Checks if ship can fit and returns True or False"""
    check = True
    # Iterates through the length of the ship
    for i in range(int(length)):
        if direction == DOWN:
            # Checks if cell is occupied iterating down the column
            if board[col + i][row] is not None:
                check = False
        if direction == RIGHT:
            # Checks if cell is occupied iterating across the row
            if board[col][row + i] is not None:
                check = False
    return check


def generate_starting_position(
    board: list[list[None]], direction: int, length: int
) -> list[int, int]:
    """Generated valid starting position depending on size of board and the
    direction and length of ship"""
    # Handles potential randint randrange error
    if len(board) - int(length) - 1 == -1:
        return [0, 0]
    if direction == DOWN:
        # Generates random starting position within the board
        starting_location = [
            randint(0, len(board) - int(length) - 1),
            randint(0, len(board) - 1),
        ]
    if direction == RIGHT:
        # Generates random starting position within the board
        starting_location = [
            randint(0, len(board) - 1),
            randint(0, len(board) - int(length) - 1),
        ]
    return starting_location


def place_battleships_simple(
    board: list[list[None]], battleships: dict[str, int]
) -> list[list]:
    """Places a battleship on each row"""
    count = 0
    # Repeats for each ship in battleships dictionary
    for ship in battleships.keys():
        # Repeats for each length of the ship
        for i in range(battleships[ship]):
            # Places the ship onto the board
            board[count][i] = ship
        count += 1
    return board


def place_battleships_random(
    board: list[list[None]], battleships: dict[str, int]
) -> list[list]:
    """Places battleships randomly onto the board"""
    # Repeats for each ship in battleships dictionary
    for ship, length in battleships.items():
        placed = False
        # Loop to check the ship has a valid placement
        while not placed:
            # Generates random direction and starting position
            direction = randint(0, 1)
            col, row = generate_starting_position(board, direction, length)
            placed = is_position_occupied(board, col, row, direction, length)

        # Places the ship onto the board depending on direction
        if direction == DOWN:
            for i in range(int(length)):
                board[col + i][row] = ship
        if direction == RIGHT:
            for i in range(int(length)):
                board[col][row + i] = ship
    return board


def place_battleships_custom(
    board: list[list[None]], battleships: dict[str, int]
) -> list[list]:
    """Custom algorithm of battleships using placement.json"""
    # Gets and constructs absolute path of file
    # This is so that the file can be accessed by any environment
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "placement.json")
    # Load ship placement data from placement.json
    with open(file_path, "r", encoding="utf-8") as placement:
        ship_data = json.load(placement)

    # Place each ship on the board based on custom placement data
    for ship, key in ship_data.items():
        # Creates variables of all ship data
        col = int(key[1])
        row = int(key[0])
        direction = key[2]
        length = battleships.get(ship)

        # Places the ship onto the board depending on direction
        if direction == "v":
            for i in range(length):
                board[col + i][row] = ship
        if direction == "h":
            for i in range(length):
                board[col][row + i] = ship

    return board


def place_battleships(
    board: list[list[None]], ships: dict[str, int], algorithm: str = "simple"
) -> list[list]:
    """Places battleships onto the board and returns it

    Keyword arguments:
    board -- a list of lists containing None
    ships -- a dictionary containing each ship and its length
    algorithm -- determines the algorithm used to place ships (default "simple")
    """
    # Checks if argument board is a list
    if not isinstance(board, list) or board is None:
        raise TypeError("Board must be a list")
    if len(board) < 5 or len(board) > 10:
        raise ValueError("Board must be between 5 and 10")

    # Checks if argument ships is a valid dictionary
    if not isinstance(ships, dict) or ships is None:
        raise TypeError("Ships must be a dictionary")

    if not all(isinstance(value, int) for value in ships.values()):
        raise TypeError("All ship dictionary values must be integers")

    # Checks if argument algorithm is a string
    if not isinstance(algorithm, str):
        raise TypeError("Algorithm must be a string")

    # Checks if ship lengths are within the board
    if max(ships.values()) > len(board) or min(ships.values()) < 1:
        raise ValueError("Invalid ship length")

    # Calls the appropriate placement algorithm
    if algorithm == "simple" and len(ships) <= len(board):
        return place_battleships_simple(board, ships)
    if algorithm == "random":
        return place_battleships_random(board, ships)
    if algorithm == "custom":
        return place_battleships_custom(board, ships)

    # Raises error if algorithm is invalid
    raise ValueError(f"Invalid algorithm type: {algorithm}")


def print_player_board(board: list[list]) -> None:
    """Prints out player's resulting board.

    Keyword arguments:
    players -- a dictionary containing player data
    username -- the username of the player
    """
    max_length = 0
    # Finds the string length of the longest cell
    for row in board:
        for cell in row:
            # Checks if cell is not empty and updates cell_length
            if cell is not None:
                cell_length = len(str(cell))
                # Updates max_length if cell_length is greater
                if cell_length > max_length:
                    max_length = cell_length

    # Prints out the board
    for row in board:
        for cell in row:
            if cell is None:
                # Prints empty cell
                print("  ~".ljust(max_length + 2), end="")
            else:
                # Prints cell with ship name
                print(f" {cell} ".ljust(max_length + 2), end="")
        # Prints new line after each row
        print()


def check_game_over(username: str, players: dict) -> bool:
    """Check if the game is over for a specific player.

    Keyword arguments:
    username -- username of the player
    players -- dictionary containing the game data of each player
    """
    # Assume game is over
    game_over = True
    # Iterate over each row in player board
    for row in players[username]["board"]:
        # Iterate over each value in row
        for value in row:
            # If a non-empty cell is found, the game is not over
            if value is not None:
                game_over = False
                break
        if not game_over:
            break
    return game_over
