from game import Game
from game.game_config import GameConfig

def main() -> None:

    config = GameConfig()
    
    game = Game(config)
    
    game.start()

    game.loop()

if __name__ == "__main__":
    main()