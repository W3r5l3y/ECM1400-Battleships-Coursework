"""Module containing game mechanics"""


def attack(coordinates, board, battleships):
    """Checks if ships has been hit and updates battleships dictionary"""
    if max(coordinates) <= len(board):
        col, row = coordinates
        if board[col][row] is not None:
            ship = board[col][row]
            board[col][row] = None
            battleships[ship] = str(int(battleships[ship]) - 1)
            return True

        return False

    print("check if battleship at coordinates")
    print("set value to none if hit")
    return True


def cli_coordinates_input():
    """Requests user input and formats into tuple"""
    while True:
        try:
            entry = str(input("Enter Coordinates...\n"))
            if len(entry) != 2:
                print("Invalid data entered!")
                continue
            coordinates = (int(entry[0]), int(entry[1]))
            return coordinates
        except (ValueError, IndexError) as err:
            print("Error:", err)


def simple_game_loop():
    print("|" + "-" * 100 + "|")
    print("Wagwan G. Battleships innit")
    print("|" + "-" * 100 + "|")
    board = components.initialise_board()
    battleships = components.create_battleships()
    board = components.place_battleships(
        board,
        battleships,
        placement="simple",
    )
    game_over = False
    while game_over is False:
        coordinates = cli_coordinates_input()
        if attack(coordinates, board, battleships) is True:
            print("HIT!")
        else:
            print("MISS!")
        for lines in board:
            print(lines)


if __name__ == "__main__":
    import components

    simple_game_loop()
    for lines in board_view:
        print(lines)
