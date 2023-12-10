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

    size = 5  # Size of grid used

    print("|" + "-" * 100 + "|")
    print("Welcome to Battleships! (MULTIPLAYER)")
    print("|" + "-" * 100 + "|")
    username = str(input("Enter your name...\n"))

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

    # Game loop
    game_over = False
    while game_over is False:
        # Processes the players coordinates on the BOT's board
        print("\nYour move.")
        player_attack = game_engine.cli_coordinates_input()
        outcome = game_engine.attack(
            player_attack, players["BOT"]["board"], players["BOT"]["battleships"]
        )
        if outcome is True:
            print("HIT!")
        else:
            print("MISS!")

        # Checks if the BOT's board is empty
        game_over = all(
            all(value is None for value in row) for row in players["BOT"]["board"]
        )
        if game_over is True:
            winner = username.upper()
            break

        # Processes the BOT's coordinates on the players board
        print("\nBot's move.")
        bot_attack = generate_attack(size)
        outcome = game_engine.attack(
            bot_attack, players[username]["board"], players[username]["battleships"]
        )
        if outcome is True:
            print("BOT HIT!")
        else:
            print("BOT MISS!")
        # Prints out players resulting board
        for row in players[username]["board"]:
            for cell in row:
                if cell is None:
                    print("  ~".ljust(7), end="")
                else:
                    print(f" {cell} ".ljust(7), end="")
            print()
        # Checks if the player's board is empty
        game_over = all(
            all(value is None for value in row) for row in players[username]["board"]
        )
        if game_over is True:
            winner = "BOT"

    # Game over message
    print("GAME OVER!")
    print(f"THE WINNER WAS {winner}!")


# Initialises dictionary to store player data
players = {}

if __name__ == "__main__":
    ai_opponent_game_loop()
