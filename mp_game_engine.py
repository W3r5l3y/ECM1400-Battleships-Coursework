"""Module containing multiplayer game mechanics"""

from random import randint
import components


def generate_attack():
    """Generates coordinates at random"""
    col = randint(0, 9)
    row = randint(0, 9)
    coordinates = (col, row)
    return coordinates


def ai_opponent_game_loop():
    """Manual testing game loop for MP"""
    print("|" + "-" * 100 + "|")
    print("Wagwan G. Battleships innit (MULTIPLAYER)")
    print("|" + "-" * 100 + "|")
    username = str(input("Enter your name..."))
    players[username] = {
        "board": components.initialise_board,
        "battleships": components.create_battleships,
    }
    players["BOT"] = {
        "board": components.initialise_board,
        "battleships": components.create_battleships,
    }


# players = {"james": {"board": [], "battleships": {}}}
players = {}
