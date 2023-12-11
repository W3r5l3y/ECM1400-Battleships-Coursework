"""Main module for project"""

import json
from flask import Flask, render_template, jsonify, request

import components as c
import game_engine as ge
import mp_game_engine as mge

# Initialise the Flask object
app = Flask(__name__)


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    """Initial placement of the ships on the board"""
    if request.method == "GET":
        return render_template(
            "placement.html", ships=player_battleships, board_size=BOARD_SIZE
        )

    if request.method == "POST":
        data = request.get_json()
        with open("placement.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return jsonify({"Success": True})

    return None


@app.route("/", methods=["GET"])
def root():
    """PLACEHOLDER"""

    # Declaring global variables
    global player_board

    if request.method == "GET":
        player_board = c.place_battleships(
            player_board, player_battleships, algorithm="custom"
        )
        players["player"]["board"] = player_board

    return render_template("main.html", player_board=player_board)


@app.route("/attack", methods=["GET"])
def process_attack():
    """PLACEHOLDER"""

    if request.args:
        try:
            player_list = list(players.keys())
            player1, player2 = player_list
            for username in player_list:
                game_over = False
                game_over = c.check_game_over(username, players)
                if game_over is True:
                    winner = player2.upper() if username == player1 else player1.upper()
                    break

            if game_over is not True:
                # Player attack on BOT's board
                row = request.args.get("x")
                col = request.args.get("y")
                player_attack = (int(col), int(row))
                outcome = ge.attack(
                    player_attack,
                    players["BOT"]["board"],
                    players["BOT"]["battleships"],
                )

                # BOT attack on Player's board
                bot_attack = mge.generate_attack(BOARD_SIZE)
                ge.attack(
                    bot_attack,
                    players["player"]["board"],
                    players["player"]["battleships"],
                )

            player_list = list(players.keys())
            player1, player2 = player_list
            for username in player_list:
                game_over = False
                game_over = c.check_game_over(username, players)
                if game_over is True:
                    winner = player2.upper() if username == player1 else player1.upper()
                    break

            if game_over is True:
                return jsonify(
                    {
                        "hit": True,
                        "Player_Turn": (row, col),
                        "AI_Turn": bot_attack,
                        "finished": (f"GAME OVER {winner} WINS!"),
                    }
                )

            return jsonify(
                {"hit": outcome, "Player_Turn": player_attack, "AI_Turn": bot_attack}
            )

        except UnboundLocalError:
            return "Game Over"

    return "Unknown Error"


# Initialises variables
BOARD_SIZE = 10
players = {}

# Initialises the boards and battleships for player and BOT
player_board = c.initialise_board(size=BOARD_SIZE)
bot_board = c.initialise_board(size=BOARD_SIZE)

player_battleships = c.create_battleships()
bot_battleships = c.create_battleships()

# Places BOT's battleships onto bot_board using random algorithm
bot_board = c.place_battleships(
    bot_board, bot_battleships, algorithm="simple"
)  # CHANGE TO RANDOM

# Saves board and battleships into player dictionaries
players["player"] = {
    "board": player_board,
    "battleships": player_battleships,
}
players["BOT"] = {
    "board": bot_board,
    "battleships": bot_battleships,
}

if __name__ == "__main__":
    # Runs the Flask app
    app.run()
