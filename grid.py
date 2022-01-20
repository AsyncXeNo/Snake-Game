import random
import pygame
from snake import Snake
from apple import Apple

class Grid(object):
    def __init__(self, application, cols, rows, boxsize):
        self.application = application
        self.cols = cols
        self.rows = rows
        self.boxsize = boxsize
        self.snake = Snake(self, [self.boxsize*self.cols//2, self.boxsize*self.rows//2], 0, 3, 'white', 'green')
        self.surface = pygame.Surface((self.cols*self.boxsize, self.rows*self.boxsize))
        self.spawn_apple()

    def spawn_apple(self):
        random_pos = random.randrange(0, self.cols * self.boxsize, self.boxsize), random.randrange(0, self.rows * self.boxsize, self.boxsize)
        while random_pos in [body_part.pos for body_part in self.snake.body]:
            random_pos = random.randrange(0, self.cols * self.boxsize, self.boxsize), random.randrange(0, self.rows * self.boxsize, self.boxsize)

        self.apple = Apple(self, random_pos, (255, 0, 0))

    def update_graphics(self):
        self.surface.fill("black")

        # Draw grid
        for i in range(1, self.cols):
            pygame.draw.line(self.surface, (165, 42, 42), (i * self.boxsize, 0), (i * self.boxsize, self.cols * self.boxsize))
        for i in range(1, self.rows):
            pygame.draw.line(self.surface, (165, 42, 42), (0, i * self.boxsize), (self.rows * self.boxsize, i * self.boxsize))

        # Draw snake
        for body_part in self.snake.body:
            pygame.draw.rect(self.surface, self.snake.color_f, (body_part.pos[0], body_part.pos[1], self.boxsize, self.boxsize), width=0)
            pygame.draw.rect(self.surface, self.snake.color_b, (body_part.pos[0], body_part.pos[1], self.boxsize, self.boxsize), width=1)

        # Draw the apple
        if self.apple:
            pygame.draw.circle(self.surface, self.apple.color, (self.apple.pos[0] + self.boxsize // 2, self.apple.pos[1] + self.boxsize // 2), self.boxsize // 2)
