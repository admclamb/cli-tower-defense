from game.pieces.wall import Wall


class GameConfig:
    size = (15, 30)
    ground_light_color = f'\033[48;5;28m▒\033[0m'
    ground_dark_color = f'\033[48;5;22m▒\033[0m'
    pieces = [
        Wall(5)
    ]
    default_currency = 200