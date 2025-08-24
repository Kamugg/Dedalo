# tests/test_maze.py
from run_dedalo.maze import Maze

def test_neighbors_center_all_valid():
    maze = Maze(3)  # internal size = 5x5
    pos = (3, 3)  # center logical cell
    neighbors = maze.get_neighbors(pos, as_list=False)

    assert neighbors['left']['pos'] == (1, 3)
    assert neighbors['right']['pos'] == (5, 3)
    assert neighbors['up']['pos'] == (3, 1)
    assert neighbors['down']['pos'] == (3, 5)

    for direction in neighbors:
        assert neighbors[direction]['is_new'] is True


def test_neighbors_corner_some_none():
    maze = Maze(2)
    pos = (1, 1)  # top-left logical cell
    neighbors = maze.get_neighbors(pos, check=False, as_list=False)

    assert neighbors['left'] is None
    assert neighbors['up'] is None
    assert neighbors['right']['pos'] == (3, 1)
    assert neighbors['down']['pos'] == (1, 3)
    assert neighbors['right']['is_new'] is True
    assert neighbors['down']['is_new'] is True
