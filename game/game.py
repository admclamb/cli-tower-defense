from game.game_config import GameConfig
from game.game_status import GameStatus
from game.map.map import Map
from game.player.wallet import Wallet
from game.round_status import RoundStatus
from game.store import Store


class Game:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.map = Map(self.config)
        self.status = GameStatus.INITIALIZED
        self.round_status = RoundStatus.PRE_ROUND
        self.player_wallet = Wallet(config.default_currency)
        self.store = Store(config.pieces)

    def start(self):
        self.status = GameStatus.RUNNING

    def loop(self):
        while self.status == GameStatus.RUNNING:
            self.map.display()
            if self.round_status == RoundStatus.PRE_ROUND:
                self.pre_round_phase()

    def pre_round_store(self) -> None:
        self.store.display(self.player_wallet)
        piece_index = int(input("Select a piece to purchase (by number): "))
        piece = self.store.purchase(piece_index, self.player_wallet)
        if piece:
            x = int(input("Enter the x-coordinate to place the piece: "))
            y = int(input("Enter the y-coordinate to place the piece: "))
            if self.map.is_within_bounds(x, y) and not self.map.is_occupied(x, y):
                self.map.place(x, y, piece)
                print(f"Placed {piece.name} at ({x}, {y})")
            else:
                print(f"Cannot place {piece.name} at ({x}, {y}). It may be out of bounds or already occupied.")

    def pre_round_phase(self):
        print("Pre-round phase: Set your towers and walls.")
        while self.round_status == RoundStatus.PRE_ROUND:
            self.pre_round_store()
            action = input("Enter action (continue (c), start round (s), quit (q)): ").strip().lower()
            if action == "s":
                self.status = GameStatus.RUNNING
                print(f"Wave starting!")
            elif action == "quit" or action == "q":
                self.status = GameStatus.GAME_OVER
                self.round_status = RoundStatus.GAME_OVER
                print("Thanks for playing!")

    def handle_user_input_pre_round(self):
        action = input("Enter action (place (p), start round (s), quit (q)): ").strip().lower()
        if action == "s":
            self.status = GameStatus.RUNNING
            print(f"Wave {self.wave_number + 1} starting!")
        elif action == "quit" or action == "q":
            self.status = GameStatus.GAME_OVER
            self.round_status = RoundStatus.GAME_OVER
            print("Thanks for playing!")