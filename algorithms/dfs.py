from dedalo.maze import Maze
import random

def dfs(maze: Maze):
    stack = []
    current_pos = maze.get_initial_pos()
    neighbors = maze.get_neighbors(current_pos)
    random.shuffle(neighbors)
    stack = neighbors + stack
    while stack:
        direction, data = stack.pop(0)
        new_pos, current_pos = data['pos'], data['orig_pos']
        if not maze.is_new(new_pos):
            continue
        maze.create_path(current_pos, direction)
        current_pos = new_pos
        yield
        neighbors = maze.get_neighbors(current_pos)
        random.shuffle(neighbors)
        stack = neighbors + stack
    return
