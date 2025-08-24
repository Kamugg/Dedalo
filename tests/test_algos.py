from algorithms.dfs import dfs
from run_dedalo.maze import Maze
from tests.validators import check_maze

test_range = [2**i for i in range(1, 9)]

def test_dfs():
    for test_size in test_range:
        maze = Maze(test_size)
        for _ in dfs(maze):
            pass
        check_maze(maze)