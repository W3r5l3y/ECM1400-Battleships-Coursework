"""Module containing game mechanics"""

import components as c


def attack(coordinates, board, battleships):
    """Checks if ships has been hit and updates battleships dictionary

    Keyword arguments:
    coordinates -- a tuple containing coordinate values
    board -- list of lists containing battleship placements
    battlships -- dictionary containing battleship name and length
    """
    if max(coordinates) < len(board):
        col, row = coordinates
        if board[col][row] is not None:
            ship = board[col][row]
            board[col][row] = None
            # Decrements length of hit ship by 1
            battleships[ship] = str(int(battleships[ship]) - 1)
            return True
        # If cell is empty
        return False
    # If coords are out of bounds
    return False


def cli_coordinates_input():
    """Requests user input and formats into tuple"""
    while True:
        try:
            entry = input("Enter Coordinates...\n")
            # Checks if entry is two characters long
            if len(entry) != 2:
                print("Invalid data entered! Please enter two numbers only.")
                continue
            # Converts entry string into tuple
            coordinates = (int(entry[0]), int(entry[1]))
            return coordinates
        except ValueError:
            print("Invalid data entered! Please enter numbers only.")
        except IndexError:
            print("Error: Index out of range.")


def simple_game_loop():
    """Manual testing game loop"""
    print("|" + "-" * 100 + "|")
    print("Welcome to Battleships! (SINGLEPLAYER))")
    print("|" + "-" * 100 + "|")

    # Initialises the board and battleships
    board = c.initialise_board()
    battleships = c.create_battleships()

    # Places battleships on the board
    board = c.place_battleships(
        board,
        battleships,
        algorithm="custom",
    )

    # Game loop
    game_over = False
    while game_over is False:
        while True:
            coordinates = cli_coordinates_input()
            # Checks if coordinates are within range of board
            if max(coordinates) < len(board):
                break
            print("Coordinates out of range!")
        if attack(coordinates, board, battleships) is True:
            print("HIT!")
        else:
            print("MISS!")
        # Prints out players resulting board
        c.print_player_board(board)
        # Checks if the board is empty (all values are None)
        game_over = all(all(value is None for value in row) for row in board)
    print("GAME OVER!")


if __name__ == "__main__":
    simple_game_loop()
