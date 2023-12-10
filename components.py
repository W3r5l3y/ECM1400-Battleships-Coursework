"""Module containing components of the game Battleships"""

from random import randint


def initialise_board(size: int = 10) -> list[list[None]]:
    """Initialises a board of size * size

    Keyword arguments:
    size -- the size of the board (default 10)
    """
    board = [[None] * size for _ in range(size)]
    return board


def create_battleships(filename: str = "battleships.txt") -> dict[str, str]:
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
            battleships[ship[0]] = ship[1]
        return battleships


def place_battleships(
    board: list[list[None]], battleships: dict[str, str], placement: str = "simple"
) -> list[list[None]]:
    """Places battleships onto the board and returns it

    Keyword arguments:
    board -- a list of lists containing None
    ships -- a dictionary containing each ship and its length
    placement -- determines the algorithm used to place ships
    """

    # Constants
    DOWN = 0
    RIGHT = 1

    def is_position_occupied(
        board: list[list[None]], col: int, row: int, direction: int, length: int
    ) -> bool:
        """Checks if ship can fit and returns True or False"""
        check = True
        for i in range(int(length)):
            if direction == DOWN:
                if board[col + i][row] is not None:
                    check = False
            if direction == RIGHT:
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
            starting_location = [
                randint(0, len(board) - int(length) - 1),
                randint(0, len(board) - 1),
            ]
        if direction == RIGHT:
            starting_location = [
                randint(0, len(board) - 1),
                randint(0, len(board) - int(length) - 1),
            ]
        return starting_location

    if placement == "simple" and len(battleships) <= len(board):
        # Places one battleship on each row
        count = 0
        for key in battleships.keys():
            for i in range(int(battleships[key])):
                board[count][i] = key
            count += 1

    elif placement == "random":
        # Places battleships randomly with random orientation
        for ship, length in battleships.items():
            placed = False
            while not placed:  # Loop to check the ship has a valid placement
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

    elif placement == "custom":
        print("Custom Placement")

    else:
        print("Invalid placement type!")

    return board


def print_player_board(board: list[list]) -> None:
    """Prints out player's resulting board.

    Keyword arguments:
    players -- a dictionary containing player data
    username -- the username of the player
    """
    for row in board:
        for cell in row:
            if cell is None:
                # Prints empty cell
                print("  ~".ljust(7), end="")
            else:
                # Prints cell with ship name
                print(f" {cell} ".ljust(7), end="")
        # Prints new line after each row
        print()
