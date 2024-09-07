
from game.config import Config
from game.game_status import GameStatus
from game.map.map import Map
from game.player.player import Player
from game.round.round_manager import RoundManager


class Game:
    def __init__(self, config: Config, round_manager: RoundManager) -> None:
        self.status = GameStatus.INITIALIZED
        self.round_manager = round_manager
        self.player = Player()
        self.map = Map(config.cols, config.rows)


    def start(self):
        self.status = GameStatus.STARTED
        self.loop()

    def loop(self):
        while self.status == GameStatus.STARTED:
            pass