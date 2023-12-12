from components import initialise_board, create_battleships, place_battleships
from game_engine import attack
from mp_game_engine import generate_attack


def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = initialise_board(size)
    # Check that the return is a list
    assert isinstance(board, list), "initialise_board function does not return a list"
    # check that the length of the list is the same as board
    assert (
        len(board) == size
    ), "initialise_board function does not return a list of the correct size"
    for row in board:
        # Check that each sub element is a list
        assert isinstance(
            row, list
        ), "initialise_board function does not return a list of lists"
        # Check that each sub list is the same size as board
        assert (
            len(row) == size
        ), "initialise_board function does not return lists of the correct size"


def test_create_battleships_return():
    """
    Test if the create_battleships function returns a dictionary consisting of
    keys of type string and values of type integer when no arguments are given.
    """
    # Get the returned values of the create_battleships function
    battleships = create_battleships()  # Default filename is "battleships.txt"

    # Check that the return is a dictionary
    assert isinstance(
        battleships, dict
    ), "create_battleships function does not return a dictionary"

    # Check that the keys are of type string
    assert all(
        isinstance(key, str) for key in battleships.keys()
    ), "create_battleships function does not return a dictionary with keys of type string"

    # Check that the values are of type integer
    assert all(
        isinstance(value, int) for value in battleships.values()
    ), "create_battleships function does not return a dictionary with values of type integer"


def test_place_battleships_return_simple():
    """
    Test if the place_battleships function returns a list of lists consisting of
    None and strings when given a board and battleships dictionary using the
    simple placement algorithm.
    """
    # Initialising variables needed for the test
    board = [
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
    battleships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    # Get the returned values of the place_battleships function
    result = place_battleships(board, battleships, algorithm="simple")

    # Check that the return is a list
    assert isinstance(result, list), "place_battleships function does not return a list"

    # Check that the list contains lists
    assert all(
        isinstance(row, list) for row in result
    ), "place_battleships function does not return a list of lists"

    # Check that the list contains strings and None
    assert all(
        isinstance(value, str) or value is None for row in result for value in row
    ), "place_battleships function does not return a list of lists consisting of strings and None"


def test_place_battleships_return_random():
    """
    Test if the place_battleships function returns a list of lists consisting of
    None and strings when given a board and battleships dictionary using the
    random placement algorithm.
    """
    # Initialising variables needed for the test
    board = [
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
    battleships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    # Get the returned values of the place_battleships function
    result = place_battleships(board, battleships, algorithm="random")

    # Check that the return is a list
    assert isinstance(result, list), "place_battleships function does not return a list"

    # Check that the list contains lists
    assert all(
        isinstance(row, list) for row in result
    ), "place_battleships function does not return a list of lists"

    # Check that the list contains strings and None
    assert all(
        isinstance(value, str) or value is None for row in result for value in row
    ), "place_battleships function does not return a list of lists consisting of strings and None"


def test_place_battleships_return_custom():
    """
    Test if the place_battleships function returns a list of lists consisting of
    None and strings when given a board, battleships dictionary and a placement.json
    file using the custom placement algorithm.
    """
    # Initialising variables needed for the test
    board = [
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
    battleships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    # Get the returned values of the place_battleships function
    result = place_battleships(board, battleships, algorithm="custom")

    # Check that the return is a list
    assert isinstance(result, list), "place_battleships function does not return a list"

    # Check that the list contains lists
    assert all(
        isinstance(row, list) for row in result
    ), "place_battleships function does not return a list of lists"

    # Check that the list contains strings and None
    assert all(
        isinstance(value, str) or value is None for row in result for value in row
    ), "place_battleships function does not return a list of lists consisting of strings and None"


def test_attack_return():
    """
    Test if the attack function returns a boolean value corresponding to whether
    the attack was a hit or miss.
    """
    # Initialising variables needed for the test
    board = [  # Ship is placed at (0, 0)
        ["Carrier", None, None],
        [None, None, None],
        [None, None, None],
    ]
    battleships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }
    hit_coordinates = (0, 0)  # Known to be a hit
    miss_coordinates = (9, 9)  # Known to be a miss
    # Get the returned values of the attack function
    result_hit = attack(hit_coordinates, board, battleships)
    result_miss = attack(miss_coordinates, board, battleships)
    # Check that the return the correct boolean value
    assert result_hit is True, "attack function does not return True for a hit"
    assert result_miss is False, "attack function does not return False for a miss"


def test_generate_attack_return():
    """
    Test if the generate_attack function returns a tuple of 2 integers within the range
    of the board both given and not given an argument of size (default = 10).
    """
    # Initialising variables needed for the test
    size = 5

    # Get the returned values of the generate_attack function
    result_no_size = generate_attack()
    result_size = generate_attack(size)

    # Check that the return is a tuple
    assert isinstance(
        result_no_size, tuple
    ), "generate_attack function does not return a tuple when no size is given"
    assert isinstance(
        result_size, tuple
    ), "generate_attack function does not return a tuple when size is given"

    # Check that the returned tuple is of length 2
    assert (
        len(result_no_size) == 2
    ), "generate_attack function does not return a tuple of length 2 when no size is given"
    assert (
        len(result_size) == 2
    ), "generate_attack function does not return a tuple of length 2 when size is given"

    # Check that the returned tuple contains integers only
    assert all(
        isinstance(value, int) for value in result_no_size
    ), "generate_attack function does not return a tuple of integers when no size is given"
    assert all(
        isinstance(value, int) for value in result_size
    ), "generate_attack function does not return a tuple of integers when no size is given"

    # Check that the returned tuple contains integers within the range of the board
    assert (
        result_no_size[0] < 10
    ), "generate_attack function does not return a tuple of integers within the range of the board when no size is given"
    assert (
        result_no_size[1] < 10
    ), "generate_attack function does not return a tuple of integers within the range of the board when no size is given"
    assert (
        result_size[0] < size
    ), "generate_attack function does not return a tuple of integers within the range of the board when size is given"
    assert (
        result_size[1] < size
    ), "generate_attack function does not return a tuple of integers within the range of the board when size is given"
