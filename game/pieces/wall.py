class Wall:
    def __init__(self,piece_cost, name="Basic Wall", symbol="\033[97m█\033[0m") -> None:
        self.name = name
        self.symbol = symbol
        self.cost = piece_cost

    def getContent(self):
        return self.symbol
    
    def getName(self):
        return self.name