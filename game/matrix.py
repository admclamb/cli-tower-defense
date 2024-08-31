class Matrix:
    def __init__(self, rows: int, cols: int, default_value = None) -> None:
        self.rows = rows
        self.cols = cols
        self.default_value = default_value
        self.grid = [[default_value for y in range(cols)] for x in range(rows)]
    
    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols
    
    def is_occupied(self, x: int, y: int) -> bool:
        return self.grid[x][y] != self.default_value

    def place(self, x: int, y: int, item) -> bool:
        if self.is_within_bounds(x, y):
            self.grid[x][y].place(item)
            return True
        return False
    
    def remove(self, x: int, y: int) -> bool:
        if self.is_within_bounds(x, y):
            self.grid[x][y].clear()
            return True
        return False
    
    def get(self, x: int, y: int):
        if self.is_within_bounds(x, y):
            return self.grid[x][y]
        return None
    
    def iterate_rows(self):
        for row in self.grid:
            yield row

    