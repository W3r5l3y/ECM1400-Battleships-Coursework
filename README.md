# ECM1400 Assessment - Battleships

## Description

The Battleships project is a classic implementation of the popular two-player strategic guessing game. It involves placing a fleet of ships on a grid and taking turns to guess the coordinates of the opponent's ships in order to sink them. This project provides a digital platform for a player to enjoy the game of Battleships in a user-friendly and interactive manner.

This project is a single player game of battleships against an BOT opponent. It utilizes Flask, a web framework in Python, in which the player can configure their board and play against an AI opponent.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/) 3.9.6
- [Flask](https://flask.palletsprojects.com/)
- [pytest](https://docs.pytest.org/en/stable/)

You can install these dependencies using the following commands:

# Install Python 3.9.6

## For Windows:

Visit [Python Downloads](https://www.python.org/downloads/release/python-396/) and download the installer. Follow the installation instructions.

## For macOS:

Open a terminal and run:

```bash
brew install python@3.9.
```

## For Linux(Debian/Ubuntu):

Open a terminal and run:

```bash
sudo apt-get update
sudo apt-get install python3.9
```

# Install Flask and pytest

```bash
pip install Flask
pip install pytest
```

Make sure to have Python and pip installed on your system before executing the commands.

## Installation

Follow these steps to install and set up the project:

1. Clone the repository: `git clone https://github.com/W3r5l3y/ECM1400-Battleships-Coursework.git`
2. Navigate to the project directory: `cd battleships`
3. Install the project using the `setup.py` file:

```bash
python setup.py install
```

This command will install the necessary dependencies and set up the project.

Optionally, you can create a virtual environment before running the above command:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
python setup.py install
```

This will create a virtual environment and install the project within it, isolating it from your system's Python environment.

## Getting Started

Run the main module to start the web server:

```bash
python main.py
```

Open your web browser and go to [http://127.0.0.1:5000/placement](http://127.0.0.1:5000/placement) to begin placing your ships on a grid.
After successfully placing your fleet and submitting the grid, you will be redirected to the root page [http://127.0.0.1:5000](http://127.0.0.1:5000). From there, you can initiate attacks on your opponent's grid until either you or the opponent emerges victorious in the game.

## Testing

To run the tests for the project, you can use the following commands for different testing modules:

### Test Components

Run this command to test the individual components of the Battleships project.

```bash
pytest test_components.py
```

Execute this command to ensure the overall functionality of the Battleships project.

```bash
pytest test_functionality.py
```

Use this command to run tests for the helper functions utilized in the Battleships project.

```bash
pytest test_helper_functions.py
```

Run this command to check the specific functionality related to student implementations.

```bash
pytest test_students.py
```

## Developer Documentation

The program is organized into four distinct modules:

- **components.py:** This module houses functions responsible for initializing either a `simple_game_loop` or an `ai_opponent_game_loop`, including tasks like board initialization and battleship placement.

- **game_engine.py:** Functions crucial for the gameplay mechanics of a `simple_game_loop` are stored in this module. This includes operations like receiving coordinate inputs from the user and executing attacks on the board.

- **mp_game_engine.py:** Dedicated to the mechanics of an `ai_opponent_game_loop`, this module encompasses additional functions. These functions involve tasks such as displaying the user's board and generating AI attacks that target the user's board.

- **main.py:** The main module orchestrates the integration of functions from the preceding modules using a Flask web interface. This integration results in the creation of an online Battleships game, providing an interactive and engaging platform for players.

## License

This project is licensed under the [MIT License](LICENSE.txt). See the [LICENSE.txt](LICENSE.txt) file for more details.

### Details

- **Author:** James Worley
- **Source code:** [GitHub Repository](https://github.com/W3r5l3y/ECM1400-Battleships-Coursework)
- **Acknowledgments:** This was the coursework project made for ECM1400 at Exeter University
