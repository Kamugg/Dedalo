from typing import Tuple, Literal, Union
import random

direction_shifts = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1),
}


class Maze(object):

    def __init__(self, size: int):
        self.size = 2*size + 1
        self.maze = [[0 for _ in range(self.size)] for _ in range(self.size)]


    def get_neighbors(self, pos: Tuple[int, int], check:bool = True, as_list:bool = True) -> Union[dict[str, dict], list[str, dict]]:
        x, y = pos
        neighbors = {}
        for name, shift in direction_shifts.items():
            new_pos = (x + 2*shift[0], y + 2*shift[1])
            if self.__valid(new_pos):
                neighbor_state = {'pos': new_pos,
                                  'is_new': self.is_new(new_pos),
                                  'orig_pos': pos}
                neighbors[name] = neighbor_state
            else:
                neighbors[name] = None
        if check:
            neighbors = {direction: data for direction, data in neighbors.items() if (data is not None) and (data['is_new'])}
        if as_list:
            neighbors = list(neighbors.items())
        return neighbors


    def create_path(self, pos: Tuple[int, int], direction: Literal['left', 'right', 'up', 'down']) -> None:
        shift = direction_shifts[direction]
        x, y = pos
        intermediate_pos = (x + shift[0], y + shift[1])
        new_pos = (x + 2*shift[0], y + 2*shift[1])
        self.maze[y][x] = 1
        self.maze[intermediate_pos[1]][intermediate_pos[0]] = 1
        self.maze[new_pos[1]][new_pos[0]] = 1


    def get_initial_pos(self) -> Tuple[int, int]:
        valid_x = [i for i in range(1, self.size, 2)]
        valid_y = [i for i in range(1, self.size, 2)]
        return random.choice(valid_x), random.choice(valid_y)


    def is_new(self, pos: Tuple[int, int]) -> bool:
        return self.maze[pos[1]][pos[0]] == 0


    def __valid(self, pos: Tuple[int, int]) -> bool:
        return (0 < pos[0] < self.size) and (0 < pos[1] < self.size)


    def __str__(self):
        maze_str = ''
        for row in self.maze:
            maze_str += ' '.join(['W' if r == 0 else 'P' for r in row]) + '\n'
        return maze_str
