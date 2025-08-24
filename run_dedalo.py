import argparse
from algorithms.dfs import dfs
from dedalo.maze import Maze
from dedalo.renderer import Renderer

ALGOS = {
    'dfs': (dfs, 'Depth First Search'),
}

def parse_args():
    algos = ["dfs"]
    parser = argparse.ArgumentParser(
        description="Dedalo – render maze generation algorithms."
    )

    parser.add_argument(
        "algorithm",
        choices=algos,
        help="Maze generation algorithm to use."
    )

    parser.add_argument(
        "--size",
        type=int,
        default=256,
        help="Size of the maze. Refers to the number of logical cells in the maze!."
    )

    return parser.parse_args()

def main():
    args = parse_args()
    maze = Maze(args.size)
    maze_gen = ALGOS[args.algorithm][0]
    maze_gen_name = ALGOS[args.algorithm][1]
    renderer = Renderer(maze, maze_gen, maze_gen_name)
    renderer.render()


if __name__ == '__main__':
    main()