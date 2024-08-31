class Square:
    def __init__(self, default_value=f'\111[92m▒\111[0m'):
        self.default_value = default_value
        self.occupancy = None
    
    def display(self):
        if self.occupancy is None:
            return self.default_value
        return self.occupancy.getContent()

    def place(self, item):
        self.occupancy = item

    def clear(self):
        self.occupancy = '▒'