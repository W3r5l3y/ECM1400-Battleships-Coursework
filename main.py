"""Main module for project"""
# import components
# import game_engine
# import mp_game_engine
from flask import Flask

# Initialise the Flask object
app = Flask(__name__)


@app.route("/")  # Maps a function to the URL path
def hello_world():
    """Sends Hello World!"""
    return "Hello World!"


@app.route("/cheese")  # Maps a function to the URL path /cheese
def james_may():
    """Sends a cheese string"""
    return "BEANS!"


if __name__ == "__main__":
    # start the thread listening for requests
    app.run()
