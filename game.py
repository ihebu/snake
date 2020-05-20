import time

import pygame

import helpers
from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 900, 600
        self.background_color = (15, 76, 129)
        self.snake_color = (237, 102, 99)
        self.snake_width = 20
        self.text_color = (232, 144, 142)
        self.font_family = "arial"
        self.font_size = 17
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.score = 0
        self.is_running = True
        self.is_frozen = True
        self.is_lost = False
        self.is_paused = False
        self.level = 30
        self.high_score = helpers.get_high_score()
        # pygame components
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.window, self.snake_color, self.snake_width)

    def listen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.snake.direction == [1, 0]:
            self.snake.direction = [-1, 0]
        if keys[pygame.K_RIGHT] and not self.snake.direction == [-1, 0]:
            self.snake.direction = [1, 0]
            self.is_frozen = False
        if keys[pygame.K_UP] and not self.snake.direction == [0, 1]:
            self.snake.direction = [0, -1]
            self.is_frozen = False
        if keys[pygame.K_DOWN] and not self.snake.direction == [0, -1]:
            self.snake.direction = [0, 1]
            self.is_frozen = False
        if keys[pygame.K_p] and not self.is_lost:
            self.pause()
        if keys[pygame.K_n] and self.is_lost:
            self.quit()
        if keys[pygame.K_y] and self.is_lost:
            self.restart()

    def pause(self):
        t2 = time.time()
        if t2 - self.t1 > 0.2:
            self.is_paused = not self.is_paused
            self.t1 = t2

    def restart(self):
        self.high_score = max(self.score, self.high_score)
        self.snake = Snake(self.window, self.snake_color, self.snake_width)
        self.is_lost = False
        self.is_frozen = True
        self.score = 0

    def run(self):
        self.window.fill(self.background_color)
        self.snake.draw_body(pygame.draw)
        self.snake.draw_food(pygame.draw)
        helpers.write_screen_stats(
            self.font, self.text_color, self.window, self.score, self.high_score
        )

    def quit(self):
        self.is_running = False
        if self.score > self.high_score:
            helpers.set_high_score(self.score)

    def levelup(self):
        self.score += 1
        self.snake.spawn_food()
        self.snake.grow()

    def lose(self):
        self.is_lost = True

    def end(self):
        pygame.quit()

    def start(self):
        self.t1 = time.time()
        while self.is_running:
            pygame.display.update()
            self.clock.tick(self.level)
            self.listen()
            self.run()
            if self.snake.ate:
                self.levelup()
            if self.snake.crashed:
                self.lose()
            if self.is_lost:
                helpers.write_on_lose(
                    self.font, self.text_color, self.window, self.score
                )
            if self.is_paused:
                helpers.write_on_pause(self.font, self.text_color, self.window)
            if not self.is_paused and not self.is_lost and not self.is_frozen:
                self.snake.move()
            if pygame.event.get(pygame.QUIT):
                self.quit()


def main():
    game = Game()
    game.start()
    game.end()


if __name__ == "__main__":
    main()
