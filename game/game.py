from game.game_config import GameConfig
from game.game_status import GameStatus
from game.map import Map
from game.round_status import RoundStatus


class Game:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.map = Map(self.config.size)
        self.status = GameStatus.INITIALIZED
        self.round_status = RoundStatus.PRE_ROUND

    def start(self):
        self.status = GameStatus.RUNNING

    def loop(self):
        while self.start == GameStatus.RUNNING:
            self.map.display()
            if self.round_status == RoundStatus.PRE_ROUND:
                self.pre_round_phase()


    def pre_round_phase(self):
        print("Pre-round phase: Set your towers and walls.")
        while self.status == GameStatus.PRE_ROUND:
            self.handle_user_input_pre_round()

    def handle_user_input_pre_round(self):
        action = input("Enter action (place, start_round, quit): ").strip().lower()
        if action == "start_round":
            self.status = GameStatus.RUNNING
            print(f"Wave {self.wave_number + 1} starting!")
        elif action == "quit":
            self.status = GameStatus.GAME_OVER
            print("Thanks for playing!")