from typing import Callable

import pygame

from dedalo.maze import Maze


class Renderer(object):

    def __init__(self, maze: Maze, maze_gen: Callable, name: str):
        self.maze = maze
        self.generator = maze_gen
        self.fps = 300
        self.clock = pygame.time.Clock()
        self.screen_size = 1539
        self.square_size = int(self.screen_size / self.maze.size)
        self.algo_name = name
        print(self.maze.size, self.screen_size, self.square_size)

    def render(self):
        pygame.init()
        display = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption(f'Dedalo - {self.algo_name} (Generating...)')
        for _ in self.generator(self.maze):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            display.fill((0, 0, 0))
            for y in range(self.maze.size):
                for x in range(self.maze.size):
                    if not self.maze.is_new((x, y)):
                        screen_x, screen_y = self.square_size*x, self.square_size*y
                        pygame.draw.rect(display, (255, 255, 255), (screen_x, screen_y, self.square_size, self.square_size))

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.display.set_caption(f'Dedalo - {self.algo_name} (Complete!)')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(30)
