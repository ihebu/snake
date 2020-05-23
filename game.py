import pygame

import helpers
from snake import Snake


class Game:
    def __init__(self):
        self.dimensions = (900, 600)
        self.bg_color = (15, 76, 129)
        self.text_color = (232, 144, 142)
        self.snake_obj = {"length": 5, "width": 20, "color": (237, 102, 99)}
        self.font_family = "arial"
        self.font_size = 17
        self.is_running = True
        self.rate = 30
        # pygame components
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.window = pygame.display.set_mode(self.dimensions)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):
        self.snake = Snake(self.window, self.snake_obj)
        self.snake.spawn_food()
        self.is_lost = False
        self.is_frozen = True
        self.score = 0

    def listen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.snake.direction = [-1, 0]
        if keys[pygame.K_RIGHT]:
            self.snake.direction = [1, 0]
            self.is_frozen = False
        if keys[pygame.K_UP]:
            self.snake.direction = [0, -1]
            self.is_frozen = False
        if keys[pygame.K_DOWN]:
            self.snake.direction = [0, 1]
            self.is_frozen = False
        if keys[pygame.K_n] and self.is_lost:
            self.end()
        if keys[pygame.K_y] and self.is_lost:
            self.start()

    def update(self):
        pygame.display.update()
        self.window.fill(self.bg_color)
        self.snake.draw_body()
        self.snake.draw_food()
        helpers.write_screen_stats(self.font, self.text_color, self.window, self.score)

    def levelup(self):
        self.score += 1
        self.snake.spawn_food()
        self.snake.grow()

    def lose(self):
        self.is_lost = True

    def run(self):
        self.clock.tick(self.rate)
        self.listen()
        self.update()
        if self.snake.ate:
            self.levelup()
        if self.snake.crashed:
            self.lose()
        if self.is_lost:
            helpers.write_on_lose(self.font, self.text_color, self.window)
        if not (self.is_lost or self.is_frozen):
            self.snake.move()
        if pygame.event.get(pygame.QUIT):
            self.end()

    def play(self):
        while self.is_running:
            self.run()

    def quit(self):
        pygame.quit()

    def end(self):
        self.is_running = False


def main():
    game = Game()
    game.play()
    game.quit()


if __name__ == "__main__":
    main()
