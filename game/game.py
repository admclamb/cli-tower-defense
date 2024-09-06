
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
        self.cursor_x = 0
        self.cursor_y = 0

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
            self.place_piece_with_keys(piece)

    def place_piece_with_keys(self, piece):
        print(f"Use arrow keys to move the piece to the desired location, then press 'Enter' to place it.")
        while True:
            self.map.display()
            self.display_cursor()
            key = keyboard.read_event()
            if key.event_type == keyboard.KEY_DOWN:
                if key.name == 'up':
                    self.cursor_y = max(0, self.cursor_y - 1)
                elif key.name == 'down':
                    self.cursor_y = min(self.map.size[0] - 1, self.cursor_y + 1)
                elif key.name == 'left':
                    self.cursor_x = max(0, self.cursor_x - 1)
                elif key.name == 'right':
                    self.cursor_x = min(self.map.size[1] - 1, self.cursor_x + 1)
                elif key.name == 'enter':
                    if self.map.is_within_bounds(self.cursor_x, self.cursor_y) and not self.map.is_occupied(self.cursor_x, self.cursor_y):
                        self.map.place(self.cursor_x, self.cursor_y, piece)
                        print(f"Placed {piece.name} at ({self.cursor_x}, {self.cursor_y})")
                        break
                    else:
                        print(f"Cannot place {piece.name} at ({self.cursor_x}, {self.cursor_y}). It may be out of bounds or already occupied.")
                        break

    def display_cursor(self):
        # This method visually marks the current cursor position on the map
        for y, row in enumerate(self.map.matrix.iterate_rows()):
            row_display = ""
            for x, square in enumerate(row):
                if x == self.cursor_x and y == self.cursor_y:
                    row_display += "[*]"  # Use an asterisk to represent the cursor
                else:
                    row_display += f" {square.display()} "
            print(row_display)

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