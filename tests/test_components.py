"""Module for testing the components used in the game Battleships"""

import pytest
from components import initialise_board, create_battleships, place_battleships

# Ideal 10x10 board
ideal_board = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
]

# Ideal battleships
ideal_ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}


# Test initialise_board
# List of different inputs and expected outputs
@pytest.mark.parametrize(
    "size, expected_exception",
    [
        (4, ValueError),
        (5, None),
        (6, None),
        (9, None),
        (10, None),
        (11, ValueError),
        (1.5, ValueError),
        (-1, ValueError),
        (0, ValueError),
        (True, ValueError),
        (None, TypeError),
        ("test", TypeError),
        ([], TypeError),
        ((), TypeError),
        ({}, TypeError),
        ("", TypeError),
    ],
)
def test_initialise_board(size, expected_exception):
    """Tests initialise_board with a range of different inputs"""
    if expected_exception is None:
        initialise_board(size)
    else:
        with pytest.raises(expected_exception):
            initialise_board(size)


# Test create_battleships
# List of different inputs and expected outputs
@pytest.mark.parametrize(
    "filename, expected_exception",
    [
        ("battleships.txt", None),
        ("test.txt", FileNotFoundError),
        ("", FileNotFoundError),
        (True, TypeError),
        (None, TypeError),
        ([], TypeError),
        ((), TypeError),
        ({}, TypeError),
        (1, TypeError),
        (1.5, TypeError),
    ],
)
def test_create_battleships(filename, expected_exception):
    """Tests create_battleships with a range of different inputs"""
    if expected_exception is None:
        create_battleships(filename)
    else:
        with pytest.raises(expected_exception):
            create_battleships(filename)


# Test place_battleships(ships)
# List of different inputs and expected outputs
@pytest.mark.parametrize(
    "board, battleships, expected_exception",
    [
        (ideal_board, {"Battleship": 5}, None),
        (ideal_board, {"Battleship": 4}, None),
        (ideal_board, {"Battleship": 3}, None),
        (ideal_board, {"Battleship": 3}, None),
        (ideal_board, {"Battleship": 2}, None),
        (ideal_board, {"Battleship": 1}, None),
        (ideal_board, {"Battleship": 11}, ValueError),
        (ideal_board, {"Battleship": 0}, ValueError),
        (ideal_board, {"Battleship": -1}, ValueError),
        (ideal_board, {"Battleship": 1.5}, TypeError),
        (ideal_board, {"Battleship": True}, None),  # Not sure whats happening here
        (ideal_board, {"Battleship": None}, TypeError),
        (ideal_board, {"Battleship": []}, TypeError),
        (ideal_board, {"Battleship": ()}, TypeError),
        (ideal_board, {"Battleship": {}}, TypeError),
        (ideal_board, {"Battleship": ""}, TypeError),
        (ideal_board, {"Battleship": "test"}, TypeError),
    ],
)
def test_place_battleships_ships(board, battleships, expected_exception):
    """Tests place_battleships with a range of different inputs"""
    if expected_exception is None:
        place_battleships(board, battleships)
    else:
        with pytest.raises(expected_exception):
            place_battleships(board, battleships)


# Test place_battleships(board)
# List of different inputs and expected outputs
@pytest.mark.parametrize(
    "board, expected_exception",
    [
        (ideal_board, None),
        ([], ValueError),
        ((), TypeError),
        ({}, TypeError),
        (1, TypeError),
        (1.5, TypeError),
        (True, TypeError),
        (None, TypeError),
        ("test", TypeError),
    ],
)
def test_place_battleships_board(board, expected_exception):
    """Tests place_battleships with a range of different inputs"""
    if expected_exception is None:
        place_battleships(board, ideal_ships)
    else:
        with pytest.raises(expected_exception):
            place_battleships(board, ideal_ships)


# Test place_battleships(algorithm)
# List of different inputs and expected outputs
@pytest.mark.parametrize(
    "algorithm, expected_exception",
    [
        ("simple", None),
        # custom not included as it requires placement.json
        ("random", None),
        ("test", ValueError),
        (1, TypeError),
        (1.5, TypeError),
        (True, TypeError),
        (None, TypeError),
        ([], TypeError),
        ((), TypeError),
        ({}, TypeError),
    ],
)
def test_place_battleships_algorithm(algorithm, expected_exception):
    """Tests place_battleships with a range of different inputs"""
    if expected_exception is None:
        place_battleships(ideal_board, ideal_ships, algorithm)
    else:
        with pytest.raises(expected_exception):
            place_battleships(ideal_board, ideal_ships, algorithm)


# Test for correct output of initialise_board
def test_initialise_board_output():
    """
    Test to verify the output of initialise_board is a list of lists of None values
    without giving an argument (default size = 10)
    """
    board = initialise_board()

    # Check the type of the output
    # Checks board is a list
    assert isinstance(board, list)
    # Checks that board is a list of lists
    assert all(isinstance(row, list) for row in board)
    # Checks that every element of the board is None
    assert all(all(element is None for element in row) for row in board)


# Test for correct output of create_battleships
def test_create_battleships_output():
    """
    Test to verify the output of create_battleships is a dictionary where the keys are strings
    and the values are integers without giving an argument (default filename = battleships.txt)
    """
    battleships = create_battleships()

    # Check the type of the output
    # Checks battleships is a dictionary
    assert isinstance(battleships, dict)
    # Checks the keys are strings and the values are integers
    assert all(isinstance(keys, str) for keys in battleships.keys())
    assert all(isinstance(values, int) for values in battleships.values())


# Test for correct output of place_battleships
def test_place_battleships_output():
    """
    Test to verify the output of place_battleships is a list of lists which contains string
    values when given 2 arguments (ideal_board, ideal_ships)
    """
    board = place_battleships(ideal_board, ideal_ships)

    # Check the type of the output
    # Checks board is a list
    assert isinstance(board, list)
    # Checks that board is a list of lists
    assert all(isinstance(row, list) for row in board)
    # Checks that there are some string values in the board
    assert any(any(isinstance(element, str) for element in row) for row in board)
