from game.game_config import GameConfig
from game.map.square import Square
from game.matrix import Matrix

class Map:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.size = config.size
        self.matrix = Matrix(self.size[0], self.size[1])
        self.initialize_squares()

    def initialize_squares(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.matrix.grid[x][y] = self.create_square(x, y)

    def create_square(self, x, y):
        # Alternate colors for a checkered pattern
        if (x + y) % 2 == 0:
            return Square(default_value=self.config.ground_dark_color)
        
        return Square(default_value=self.config.ground_light_color)

    def is_within_bounds(self, x, y):
        return self.matrix.is_within_bounds(x, y)

    def is_occupied(self, x, y):
        return self.matrix.is_occupied(x, y)
    
    def display(self) -> None:
        # Print the x-axis labels (numbers)
        x_labels = [f"{i+1:2}" for i in range(self.size[1])]
        print("  " + " ".join(x_labels))

        for y, row in enumerate(self.matrix.iterate_rows(), start=1):
            row_display = " ".join([f"{square.display():^2}" if square is not None else "  " for square in row])
            print(f"{y:2} {row_display}")