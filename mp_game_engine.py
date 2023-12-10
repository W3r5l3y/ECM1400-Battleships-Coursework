"""Module containing multiplayer game mechanics"""

from random import randint
import components
import game_engine


def generate_attack(size):
    """Generates coordinates at random"""
    col = randint(0, size - 1)
    row = randint(0, size - 1)
    coordinates = (col, row)
    return coordinates


def ai_opponent_game_loop():
    """Manual testing game loop for MP"""

    size = 10  # Size of grid used

    print("|" + "-" * 100 + "|")
    print("Wagwan G. Battleships innit (MULTIPLAYER)")
    print("|" + "-" * 100 + "|")
    username = str(input("Enter your name..."))

    # Initialises the boards and battleships for player and BOT
    player_board = components.initialise_board(size=size)
    player_battleships = components.create_battleships()

    bot_board = components.initialise_board(size=size)
    bot_battleships = components.create_battleships()

    # Saves board and battleships into player dictionaries
    players[username] = {
        "board": player_board,
        "battleships": player_battleships,
    }
    players["BOT"] = {
        "board": bot_board,
        "battleships": bot_battleships,
    }

    # Places battleships on each players board
    players[username]["board"] = components.place_battleships(
        player_board, player_battleships, placement="simple"
    )  # must be CUSTOM
    players["BOT"]["board"] = components.place_battleships(
        bot_board, bot_battleships, placement="random"
    )
    # Processes the players coordinates on the BOT's board
    player_attack = game_engine.cli_coordinates_input()
    game_engine.attack(player_attack, bot_board, bot_battleships)


# players = {"james": {"board": [], "battleships": {}}}
players = {}
if __name__ == "__main__":
    ai_opponent_game_loop()
