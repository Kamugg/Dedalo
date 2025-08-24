# tests/test_maze.py
from dedalo.maze import Maze

def test_neighbors_center_all_valid():
    maze = Maze(3)  # internal size = 5x5
    pos = (3, 3)  # center logical cell
    neighbors = maze.get_neighbors(pos)

    assert neighbors['left']['pos'] == (1, 3)
    assert neighbors['right']['pos'] == (5, 3)
    assert neighbors['up']['pos'] == (3, 1)
    assert neighbors['down']['pos'] == (3, 5)

    for direction in neighbors:
        assert neighbors[direction]['walled'] is True


def test_neighbors_corner_some_none():
    maze = Maze(2)
    pos = (1, 1)  # top-left logical cell
    neighbors = maze.get_neighbors(pos)

    assert neighbors['left'] is None
    assert neighbors['up'] is None
    assert neighbors['right']['pos'] == (3, 1)
    assert neighbors['down']['pos'] == (1, 3)
    assert neighbors['right']['walled'] is True
    assert neighbors['down']['walled'] is True
