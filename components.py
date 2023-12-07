"""Module containing components of the game Battleships"""


def initialise_board(size=10):
    """Initialises a board of size * size

    Keyword arguments:
    size -- the size of the board (default 10)
    """
    board = [[None] * size for _ in range(size)]
    return board


def create_battleships(filename="battleships.txt"):
    """Creates

    Keyword arguments:
    filename -- the name of the file to read the battleships from (default "battleships.txt")
    """
    return filename
