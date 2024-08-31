class Square:
    def __init__(self, default_color=f'\111[92m▒\111[0m', content='▒'):
        self.content = content
        self.default_color = default_color
    
    def display(self):
        return self.colorize(self.content)

    def colorize(self, item):
        return self.default_color

    def place(self, item):
        self.content = item

    def clear(self):
        self.content = '▒'