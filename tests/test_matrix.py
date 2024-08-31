import pytest
from game.matrix import Matrix

def test_matrix_initialization_cols():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    assert matrix.cols == cols
    assert len(matrix.grid[0]) == cols

def test_matrix_initialization_rows():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    assert matrix.rows == rows
    assert len(matrix.grid) == rows

def test_matrix_initialization_default_value_of_none():
    rows, cols = 5, 5
    expected_default_value = None
    matrix = Matrix(rows, cols, expected_default_value)

    for row in matrix.grid:
        for cell in row:
            assert cell is expected_default_value

def test_matrix_initialization_default_value_of_empty_string():
    rows, cols = 5, 5
    expected_default_value = ''
    matrix = Matrix(rows, cols, expected_default_value)

    for row in matrix.grid:
        for cell in row:
            assert cell is expected_default_value

def test_if_is_within_bounds():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    assert matrix.is_within_bounds(0, 0) == True
    assert matrix.is_within_bounds(4, 4) == True
    assert matrix.is_within_bounds(5, 5) == False
    assert matrix.is_within_bounds(-1, -1) == False

def test_is_occupied():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    item = "test item"

    matrix.place(0, 0, item)

    assert matrix.is_occupied(0, 0) == True

def test_is_not_occupied():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    assert matrix.is_occupied(1, 1) == False

def test_place_item():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    expected_item = "Test item"

    assert matrix.place(1, 1, expected_item) == True
    assert matrix.grid[1][1] == expected_item

def test_remove_item():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)
    item = "Tower"
    
    matrix.place(2, 2, item)
    assert matrix.grid[2][2] == item
    
    assert matrix.remove(2, 2) == True
    assert matrix.grid[2][2] is None

def test_remove_item_on_fail():
    rows, cols = 5, 5
    matrix = Matrix(rows, cols)

    assert matrix.remove(2, 2) == False

def test_get_item():
    matrix = Matrix(5, 5)
    item = "Tower"
    
    matrix.place(3, 3, item)
    assert matrix.get(3, 3) == item
    
    assert matrix.get(4, 4) is None