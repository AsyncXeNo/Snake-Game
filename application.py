import pygame
from grid import Grid


class Application(object):
    def __init__(self):
        pygame.init()

        self.win = pygame.display.set_mode((640, 640))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.grid = Grid(self, 30, 30, 20)
        self.starting_pos = (25, 25)

        self.score = 0

        self.move_snake = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_snake, 100)

    def run_main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.move_snake:
                    self.grid.snake.move()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    if self.grid.snake.direction == 3:
                        self.grid.snake.direction = 0
                    else: self.grid.snake.direction += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    if self.grid.snake.direction == 0:
                        self.grid.snake.direction = 3
                    else: self.grid.snake.direction -= 1
            
            self.clock.tick(self.fps)
            self.win.fill("black")
            self.grid.update_graphics()
            self.win.blit(self.grid.surface, (20, 20))
            pygame.display.update()

    def game_over(self):
        print(f"Game Over. Score: {self.score}")
        exit()
