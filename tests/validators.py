from itertools import product

from run_dedalo.maze import Maze


def check_wall_integrity(maze: Maze):
    assert sum(maze.maze[0]) == 0
    assert sum(maze.maze[-1]) == 0
    assert sum([maze.maze[i][0] for i in range(maze.size)]) == 0
    assert sum([maze.maze[i][-1] for i in range(maze.size)]) == 0


def check_odd_cells(maze: Maze):
    odds = range(1, maze.size, 2)
    for x, y in product(odds, odds):
        assert maze.maze[y][x] == 1


def check_even_cells(maze: Maze):
    even = range(2, maze.size, 2)
    for x, y in product(even, even):
        assert maze.maze[y][x] == 0


def check_connected_cells(maze: Maze):
    odds = range(1, maze.size, 2)
    for x, y in product(odds, odds):
        neighbors = maze.get_neighbors((x, y), check=False)
        neighbors = [n for n in neighbors if (n[1] is not None) and not(n[1]['is_new'])]
        assert len(neighbors) >= 1


def spanning_sum(maze: Maze):
    assert sum([sum(row) for row in maze.maze]) == 2*int((maze.size-1)/2)**2 - 1


def connected(maze: Maze):
    start_pos = maze.get_initial_pos()
    stack = [{'new': start_pos, 'old': None}]
    table = set()
    while stack:
        step = stack.pop(0)
        new_pos = step['new']
        old_pos = step['old']
        assert new_pos not in table
        table.add(new_pos)
        x, y = new_pos
        neighbors = [
            {'new': (x+1, y), 'old': (x, y)},
            {'new': (x-1, y), 'old': (x, y)},
            {'new': (x, y-1), 'old': (x, y)},
            {'new': (x, y+1), 'old': (x, y)},
        ]
        neighbors = [n for n in neighbors if (maze.maze[n['new'][1]][n['new'][0]]==1) and (n['new'] != old_pos)]
        stack += neighbors


def check_maze(maze: Maze):
    check_wall_integrity(maze)
    check_odd_cells(maze)
    check_even_cells(maze)
    check_connected_cells(maze)
    spanning_sum(maze)
    connected(maze)