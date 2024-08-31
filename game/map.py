from game.matrix import Matrix


class Map:
    def __init__(self, size=(25, 25)) -> None:
        self.size = size
        self.matrix = Matrix(size[0], size[1])

    def is_within_bounds(self, x, y):
        return self.matrix.is_within_bounds(x, y)

    def is_occupied(self, x, y):
        return self.matrix.is_occupied(x, y)
    
    def display(self) -> None:
        print(self.matrix.display)