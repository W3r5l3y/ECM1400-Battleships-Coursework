"""Module containing components of the game Battleships"""

from random import randint
import json

# Constants
DOWN = 0
RIGHT = 1


def initialise_board(size: int = 10) -> list[list[None]]:
    """Initialises a board of size * size

    Keyword arguments:
    size -- the size of the board (default 10)
    """
    board = [[None] * size for _ in range(size)]
    return board


def create_battleships(filename: str = "battleships.txt") -> dict[str, int]:
    """Reads the text file and returns battleships as a dictionary

    Keyword arguments:
    filename -- name of file containing battleship data (default "battleships.txt")
    """
    battleships = {}
    # Opens file and reads each line
    with open(filename, "r", encoding="utf-8") as f:
        filelines = f.readlines()
        for line in filelines:
            # Splits each line into ship name and length and adds to dictionary
            ship = line.strip().split(":")
            battleships[ship[0]] = int(ship[1])
        return battleships


def is_position_occupied(
    board: list[list[None]], col: int, row: int, direction: int, length: int
) -> bool:
    """Checks if ship can fit and returns True or False"""
    check = True
    for i in range(int(length)):
        # Iterates through the length of the ship
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
) -> list[list[None]]:
    """Places a battleship on each row"""
    count = 0
    for ship in battleships.keys():
        # Repeats for each ship
        for i in range(battleships[ship]):
            # Repeats for the length of the ship
            board[count][i] = ship
        count += 1
    return board


def place_battleships_random(
    board: list[list[None]], battleships: dict[str, int]
) -> list[list[None]]:
    """Places battleships randomly onto the board"""
    for ship, length in battleships.items():
        # Repeats for each ship
        placed = False
        while not placed:
            # Loop to check the ship has a valid placement
            direction = randint(0, 1)
            col, row = generate_starting_position(board, direction, length)
            placed = is_position_occupied(board, col, row, direction, length)

        # Places the ship onto the board
        if direction == DOWN:
            for i in range(int(length)):
                board[col + i][row] = ship
        if direction == RIGHT:
            for i in range(int(length)):
                board[col][row + i] = ship
    return board


def place_battleships_custom(
    board: list[list[None]], battleships: dict[str, int]
) -> list[list[None]]:
    """Custom algorithm of battleships using placement.json"""

    with open("placement.json", "r", encoding="utf-8") as placement:
        ship_data = json.load(placement)
    for ship, key in ship_data.items():
        col = int(key[0])
        row = int(key[1])
        direction = key[2]
        length = battleships.get(ship)
        # Places the ship onto the board
        if direction == "v":
            for i in range(int(length)):
                board[col + i][row] = ship
        if direction == "h":
            for i in range(int(length)):
                board[col][row + i] = ship

    return board


def place_battleships(
    board: list[list[None]], ships: dict[str, int], algorithm: str = "simple"
) -> list[list[None]]:
    """Places battleships onto the board and returns it

    Keyword arguments:
    board -- a list of lists containing None
    ships -- a dictionary containing each ship and its length
    algorithm -- determines the algorithm used to place ships (default "simple")
    """
    if algorithm == "simple" and len(ships) <= len(board):
        return place_battleships_simple(board, ships)
    if algorithm == "random":
        return place_battleships_random(board, ships)
    if algorithm == "custom":
        return place_battleships_custom(board, ships)

    # Will return original board if algorithm arg is invalid
    print("Invalid algorithm type!")
    return board


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
