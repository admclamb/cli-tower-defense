# Tower Defense Game

A Python CLI tower defense game where you place towers and walls to defend your base from waves of enemies.

## Features

- Place towers and walls to defend your base.
- Waves of enemies that follow the shortest path to your base.
- Strategy-based gameplay.

## Project Structure

- `game/`: Contains all the game logic and components.
- `test/`: Contains all the tests for the game using `pytest`.

## Requirements

- Python 3.8+
- `pytest` for testing
- `mypy` for type checking

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tower-defense-game.git
   cd tower-defense-game
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install --editable .
   ```

## Running the Game

To start the game, run:

```bash
tower-defense
```

## Testing

To run the tests, use:

```bash
pytest
```

## Type Checking

To run `mypy` for static type checking, use:

```bash
mypy game/
```

## Contributing

Feel free to fork this repository and submit pull requests.

## License

[Your License Here]
