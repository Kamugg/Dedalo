from dedalo.maze import Maze

def dfs(maze: Maze):
    stack = []
    current_pos = (3, 3)
    n = maze.get_neighbors(current_pos)
    stack = [(k, v['pos']) for k, v in n.items() if (v is not None) and v['is_new']] + stack
    while stack:
        print(stack)
        d, p = stack.pop(0)
        while maze.maze[p[1]][p[0]] == 1:
            if stack:
                d, p = stack.pop(0)
            else:
                break
        if not stack and maze.maze[p[1]][p[0]] == 1:
            continue
        maze.create_path(current_pos, d)
        current_pos = p
        yield
        n = maze.get_neighbors(current_pos)
        stack = [(k, v['pos']) for k, v in n.items() if (v is not None) and v['is_new']] + stack
    return

maze = Maze(10)
count = 0
print(maze)
for _ in dfs(maze):
    print(maze)