import pytest
from components import initialise_board


def test_initialise_board_with_boundary_cases():
    sizes = [4, 5, 6, 9, 10, 11]
    for size in sizes:
        # Range of unacceptable values
        if size < 5 or size > 10:
            with pytest.raises(ValueError):
                initialise_board(size)
        else:
            initialise_board(size)


def test_initialise_board_with_non_int():
    with pytest.raises(ValueError):
        initialise_board(1.5)


def test_initialise_board_with_negative_int():
    with pytest.raises(ValueError):
        initialise_board(-1)


def test_initialise_board_with_zero():
    with pytest.raises(ValueError):
        initialise_board(0)


def test_initialise_board_with_string():
    with pytest.raises(TypeError):
        initialise_board("test")


def test_initialise_board_with_none():
    with pytest.raises(TypeError):
        initialise_board(None)


def test_initialise_board_with_empty():
    # Expected outcome
    board = [[None] * 10 for _ in range(10)]
    # Actual outcome
    result = initialise_board()
    # Assertion
    assert result == board


def test_initialise_board_with_list():
    with pytest.raises(TypeError):
        initialise_board([])


def test_initialise_board_with_tuple():
    with pytest.raises(TypeError):
        initialise_board(())


def test_initialise_board_with_dict():
    with pytest.raises(TypeError):
        initialise_board({})
