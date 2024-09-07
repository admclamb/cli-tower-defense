from game.map.square import Square


class Map:
    def __init__(self, cols: int, rows: int, square: Square) -> None:
        self.cols = cols
        self.rows = rows
        self.grid = [[square for _ in range(cols)] for _ in range(rows)]
