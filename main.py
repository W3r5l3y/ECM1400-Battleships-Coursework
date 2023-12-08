"""Main module for project"""

import components

import game_engine


print("|" + "-" * 100 + "|")
board = components.initialise_board()
battleships = components.create_battleships()
board_view = components.place_battleships(
    board,
    battleships,
    placement="simple",
)
"""
for lines in board_view:
    print(lines)
"""

game_engine.attack((0, 1), board, battleships)
for lines in board_view:
    print(lines)
