"""
This module contains the multiplayer game logic for the Battleships game, 
where the player competes against a bot.

It includes functions for generating random attacks within the board, and a game loop 
for testing the game against an AI opponent. The game logic is handled by the 'game_engine' 
and 'components' modules, which are imported as 'ge' and 'c' respectively.

The main functions in this module are as follows:

The `generate_attack` function generates a random attack for the bot within 
the board and returns it as a tuple. 
The `ai_opponent_game_loop` function is a manual testing game loop 
where the player can play against the bot.

This module is used by the main server module to handle the game logic.
"""

from random import randint
import components as c
import game_engine as ge


def generate_attack(size: int = 10):
    """Generates coordinates at random"""
    # Generates random col and row within the board
    col = randint(0, size - 1)
    row = randint(0, size - 1)
    # Puts col and row into a tuple
    coordinates = (col, row)
    return coordinates


def ai_opponent_game_loop() -> None:
    """Manual testing game loop for MP"""

    size = 10  # Size of grid used

    # Prints welcome message
    print("|" + "-" * 100 + "|")
    print("Welcome to Battleships! (MULTIPLAYER)")
    print("|" + "-" * 100 + "|")

    # Asks player for username
    username = str(input("Enter your name...\n"))

    # Initialises the boards and battleships for player and BOT
    player_board = c.initialise_board(size=size)
    player_battleships = c.create_battleships()

    bot_board = c.initialise_board(size=size)
    bot_battleships = c.create_battleships()

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
    players[username]["board"] = c.place_battleships(
        player_board, player_battleships, algorithm="simple"
    )  # must be CUSTOM
    players["BOT"]["board"] = c.place_battleships(
        bot_board, bot_battleships, algorithm="random"
    )

    # Game loop
    game_over = False
    while game_over is False:
        # Player's turn
        print("\nYour move.")
        # Loop to get valid coordinates from user
        while True:
            player_attack = ge.cli_coordinates_input()
            # Checks if coordinates are within range of board
            if max(player_attack) < size:
                break
        # Processes the players coordinates on the BOT's board
        outcome = ge.attack(
            player_attack, players["BOT"]["board"], players["BOT"]["battleships"]
        )
        # Checks if attack was successful and prints result
        if outcome is True:
            print("HIT!")
        else:
            print("MISS!")

        # Checks if the BOT's board is empty
        game_over = all(
            all(value is None for value in row) for row in players["BOT"]["board"]
        )
        # Checks if game is over and announces winner
        if game_over is True:
            winner = username.upper()
            break

        # BOT's turn
        print("\nBot's move.")
        # Generates BOT's coordinates
        bot_attack = generate_attack(size)
        # Processes the BOT's coordinates on the player's board
        outcome = ge.attack(
            bot_attack, players[username]["board"], players[username]["battleships"]
        )
        # Checks if BOT attack was successful and prints result
        if outcome is True:
            print("BOT HIT!")
        else:
            print("BOT MISS!")
        # Prints out players resulting board
        c.print_player_board(players[username]["board"])
        # Checks if the player's board is empty
        game_over = all(
            all(value is None for value in row) for row in players[username]["board"]
        )
        # Checks if game is over and announces BOT as winner
        if game_over is True:
            winner = "BOT"

    # Game over message
    print("GAME OVER!")
    print(f"THE WINNER WAS {winner}!")


# Initialises dictionary to store player data
players = {}

if __name__ == "__main__":
    ai_opponent_game_loop()
