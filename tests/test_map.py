import pytest
from game.map import Map

def test_map_initialization_size():
    size = (25, 25)
    map = Map(size)

    assert map.size[0] == size[0]
    assert map.size[1] == size[1]