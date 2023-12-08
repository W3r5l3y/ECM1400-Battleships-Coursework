"""Module containing components of the game Battleships"""

from random import randint


def initialise_board(size=10):
    """Initialises a board of size * size

    Keyword arguments:
    size -- the size of the board (default 10)
    """
    board = [[None] * size for _ in range(size)]
    return board


def create_battleships(filename="battleships.txt"):
    """Reads the text file and returns battleships as a dictionary

    Keyword arguments:
    filename -- name of file containing battleship data (default "battleships.txt")
    """
    battleships = {}
    with open(filename, "r", encoding="utf-8") as f:
        filelines = f.readlines()
        for line in filelines:
            ship = line.strip().split(":")
            battleships[ship[0]] = ship[1]
        return battleships


def place_battleships(board, battleships, placement="simple"):
    """Places battleships onto the board and returns it

    Keyword arguments:
    board -- a list of lists containing None
    ships -- a dictionary containing each ship and its length
    placement -- determines the algorithm used to place ships
    """

    # Constants
    DOWN = 0
    RIGHT = 1

    def is_position_occupied(board, col, row, direction, length):
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

    def generate_starting_position(board, direction, length):
        """Generated valid starting position depending on direction of ship"""
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
        count = 0
        for key in battleships.keys():
            for i in range(int(battleships[key])):
                board[count][i] = key
            count += 1

    elif placement == "random":
        for ship, length in battleships.items():
            placed = False
            while not placed:  # Loop to check the ship has a valid placement
                direction = randint(0, 1)
                col, row = generate_starting_position(board, direction, length)
                placed = is_position_occupied(board, col, row, direction, length)
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


# x = place_battleships(initialise_board(), create_battleships(), placement="random")
# for item in x:
# print(item)
# print(initialise_board(), "\n", create_battleships())
