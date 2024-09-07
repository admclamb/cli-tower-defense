
from game.config import Config
from game.game import Game


def setup_game():
    config = Config()
    game = Game(config)

    return game

def main():
    game = setup_game()
    game.start()

if __name__ == "__main__":
    main()