def initialise_board(size=10):
    board = [[""] * size for _ in range(size)]
    return board


print(initialise_board(5))
