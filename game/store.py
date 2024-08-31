from game.pieces import wall
from game.player.wallet import Wallet


class Store:
    def __init__(self, available_pieces) -> None:
        self.available_pieces = available_pieces

    def display(self, player_wallet: Wallet) -> None:
        print(f"Currency: {player_wallet.currency}")
        print("Available Pieces:")
        for index, piece in enumerate(self.available_pieces, start=1):
            print(f"{index}. {piece.symbol} : {piece.name} - Cost: {piece.cost}")

    def purchase(self, index: int, player_wallet: Wallet) -> None:
        if index < 1 or index > len(self.available_pieces):
            print("Purchase selection is outside the bounds.")
            return None
        
        piece = self.available_pieces[index - 1]
        if player_wallet.currency >= piece.cost:
            player_wallet.take(piece.cost)
            print(f"Purchased {piece.name} for {piece.cost} currency. Remaining currency: {player_wallet.currency}")
            return piece
        else:
            print(f"Not enough currency to purchase {piece.name}.")
            return None