"""Main module for project"""

import os
import json
from flask import Flask, render_template, jsonify, request

import components as c
import game_engine as ge
import mp_game_engine as mge

# Initialise the Flask object
app = Flask(__name__)


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    """
    Handles the initial placement of the ships on the board.

    This function serves a dual purpose depending on the HTTP method used.

    If a GET request is made, it returns a rendered template of the game board
    and the player can place their battleships onto the board.

    If a POST request is made, it receives the ship placement data from the
    webpage and writes the ship placement data to a JSON file.
    """

    if request.method == "GET":
        # Shows the placement.html template where the player can place battleships
        return render_template(
            "placement.html", ships=player_battleships, board_size=BOARD_SIZE
        )

    if request.method == "POST":
        # Requests ship placement data from webpage
        data = request.get_json()
        # Gets and constructs absolute path of file
        # This is so that the file can be accessed by any environment
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "placement.json")
        # Opens placement.json to write to file
        with open(file_path, "w", encoding="utf-8") as json_file:
            # Writes placement data to file
            json.dump(data, json_file, indent=4)
        # Returns success message
        return jsonify({"Success": True})

    return None


@app.route("/", methods=["GET"])
def root():
    """
    Handles the root route of the application. During normal gameplay,
    this route is only called once

    This function is called after the player has places their battleships and sends
    a GET request to the "/" route. It places battleships on the player's board
    according to their choice on /placement. This is done by reading the ship placement
    data from the placement.json file through the place_battleships function.
    The player's board data is then passed to the main.html template.
    """

    # Declaring global variable
    global player_board

    if request.method == "GET":
        # Places battleships on players board according to their choice on /placement
        # This is done by reading the ship placements from the placement.json file
        player_board = c.place_battleships(
            player_board, player_battleships, algorithm="custom"
        )
        # Updates player data dictionary with board with battleships placed
        players["player"]["board"] = player_board

    # Returns the main.html template with the player's board data
    return render_template("main.html", player_board=player_board)


@app.route("/attack", methods=["GET"])
def process_attack():
    """
    Processes an attack made when the player clicks on the grid.

    This function is called when a GET request is made to the "/attack" route.
    It reads the attack coordinates from the request arguments (where the player clicks
    on the board) and plays one turn of battleships. This function processes the turns
    of both the player and the BOT and will check if the game is over each turn.
    When game is over, GET requests made to the "/attack" route will be ignored
    therefore preventing further attacks.
    """

    if request.args:
        try:
            # Checks if game is over
            player_list = ["player", "BOT"]
            for username in player_list:
                game_over = False
                game_over = c.check_game_over(username, players)
                if game_over is True:
                    winner = "BOT" if username == "player" else "PLAYER"
                    break

            # Attack phase
            if game_over is not True:
                # Player attack on BOT's board
                # Requests attack coordinates from request arguments
                # Loops until bot move is unique
                row = request.args.get("x")
                col = request.args.get("y")
                player_attack = (int(col), int(row))
                # Checks if attack has already been played
                if player_attack in player_already_attacked:
                    # If attack has already been played, stops function here
                    return "Already Attacked"
                # Adds player attack to list to prevent repeat attacks on same coordinates
                player_already_attacked.append(player_attack)
                # Performs attack on bot board and returns hit or miss as True or False
                outcome = ge.attack(
                    player_attack,
                    players["BOT"]["board"],
                    players["BOT"]["battleships"],
                )

                # BOT attack on Player's board
                # Loops until bot move is unique
                while True:
                    bot_attack = mge.generate_attack(BOARD_SIZE)
                    # Checks if attack has already been played
                    if bot_attack not in bot_already_attacked:
                        break
                # Adds bot attack to list for comparison
                bot_already_attacked.append(bot_attack)
                # Performs attack on player board
                ge.attack(
                    bot_attack,
                    players["player"]["board"],
                    players["player"]["battleships"],
                )

            # Checks if game is over
            player_list = ["player", "BOT"]
            for username in player_list:
                game_over = False
                game_over = c.check_game_over(username, players)
                if game_over is True:
                    winner = "BOT" if username == "player" else "PLAYER"
                    break

            # If game over send game over message
            if game_over is True:
                if winner == "BOT":
                    # If BOT wins send only BOT coordinates
                    return jsonify(
                        {
                            "hit": False,
                            "AI_Turn": bot_attack,
                            "finished": (f"GAME OVER {winner} WINS!"),
                        }
                    )

                # If player wins send only player coordinates
                return jsonify(
                    {
                        "hit": True,
                        "Player_Turn": (row, col),
                        "finished": (f"GAME OVER {winner} WINS!"),
                    }
                )
            # If game not over send both player coordinates
            return jsonify(
                {"hit": outcome, "Player_Turn": player_attack, "AI_Turn": bot_attack}
            )

        # If game over send game over message and prevent further attacks
        except UnboundLocalError:
            return "Game Over"

    return "Unknown Error"


# Initialises variables
BOARD_SIZE = 10
players = {}
bot_already_attacked = []
player_already_attacked = []

# Initialises the boards and battleships for player and BOT
player_board = c.initialise_board(size=BOARD_SIZE)
bot_board = c.initialise_board(size=BOARD_SIZE)

player_battleships = c.create_battleships()
bot_battleships = c.create_battleships()

# Places BOT's battleships onto bot_board using random algorithm
bot_board = c.place_battleships(bot_board, bot_battleships, algorithm="random")

# Saves board and battleships into players dictionary
players = {
    "player": {
        "board": player_board,
        "battleships": player_battleships,
    },
    "BOT": {
        "board": bot_board,
        "battleships": bot_battleships,
    },
}

if __name__ == "__main__":
    # Runs the Flask app
    app.run()
