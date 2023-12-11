"""Main module for project"""

from flask import Flask, render_template, jsonify, request
import components

# import game_engine
# import mp_game_engine

# Initialise the Flask object
app = Flask(__name__)


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    """Initial placement of the ships on the board"""
    ships = components.create_battleships()
    board_size = 10

    if request.method == "GET":
        return render_template("placement.html", ships=ships, board_size=board_size)

    if request.method == "POST":
        data = request.get_json()
        print(data)
        return jsonify({"Success": True})

    return None


@app.route("/", methods=["GET"])
def root():
    """PLACEHOLDER"""
    board = components.initialise_board()
    if request.method == "GET":
        return 404

    return render_template("main.html", player_board=board)


@app.route("/attack", methods=["GET"])
def process_attack():
    """PLACEHOLDER"""
    game_over = False
    if request.args:
        x = request.args.get("x")
        y = request.args.get("y")
        print(x, y)
        if game_over is True:
            return jsonify(
                {
                    "hit": True,
                    "Player_Turn": (x, y),
                    "AI_Turn": (1, 2),
                    "finished": "GAME OVER",
                }
            )
        return jsonify({"hit": True, "Player_Turn": (x, y), "AI_Turn": (1, 2)})
    return None


if __name__ == "__main__":
    # Runs the Flask app
    app.run()
