
from game.game_status import GameStatus
from game.map.map import Map
from game.player.player import Player
from game.round_manager import RoundManager


class Game:
    def __init__(self, round_manager: RoundManager, player: Player, map: Map) -> None:
        self.status = GameStatus.INITIALIZED


    def start(self):
        self.status = GameStatus.STARTED

    def loop(self):
        while self.status == GameStatus.STARTED:
            pass