class Matrix:
    def __init__(self, rows: int, cols: int, default_value=None) -> None:
        self.rows = rows
        self.cols = cols
        self.default_value = default_value
        self.grid = [[default_value for _ in range(cols)] for _ in range(rows)]
    
    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols
    
    def is_occupied(self, x: int, y: int) -> bool:
        return self.grid[x][y] is not None
    
    def place(self, x: int, y: int, item) -> bool:
        if self.is_within_bounds(x, y) and not self.is_occupied(x,y):
            self.grid[x][y] = item
            return True
        return False
    
    def remove(self, x: int, y: int) -> bool:
        if self.is_within_bounds(x, y) and self.is_occupied(x, y):
            self.grid[x][y] = self.default_value
            return True
        return False
    
    def get(self, x: int, y: int):
        if self.is_within_bounds(x, y):
            return self.grid[x][y]
        return self.default_value
    
    def display(self):
        for row in self.grid:
            print(" ".join([str(item) if item else "." for item in row]))