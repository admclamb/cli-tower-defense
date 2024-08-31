from enum import Enum

class GameStatus(Enum):
    INITIALIZED = "Initialized"
    RUNNING = "Running"
    PAUSED = "Paused"
    GAME_OVER = "Game Over"