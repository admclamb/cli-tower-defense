import pytest
from game.game import Game
from game.game_config import GameConfig
from game.game_status import GameStatus
from game.map import Map

def test_game_initialization():
    config = GameConfig()
    game = Game(config)

    assert game.config == config
    assert game.status == GameStatus.INITIALIZED
    assert isinstance(game.map, Map)

def test_game_start():
    config = GameConfig()
    game = Game(config)

    game.start()
    assert game.status == GameStatus.RUNNING