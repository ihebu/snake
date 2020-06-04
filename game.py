import pygame

from snake import Snake

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (32, 138, 174)
RED = (219, 51, 17)
GREEN = (22, 226, 11)
YELLOW = (255, 212, 0)


class Game:
    def __init__(self):
        self.dimensions = (900, 600)
        self.bg_color = BLACK
        self.font_color = WHITE
        self.snake_obj = {
            "length": 5,
            "size": 20,
            "body_color": GREEN,
            "food_color": RED,
        }
        # snake size should divide window dimensions
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

    def write(self, text):
        text = self.font.render(text, True, self.font_color)
        self.window.blit(text, (10, 10))

    @property
    def text(self):
        if self.is_lost:
            return "Play Again ? ( Y / N )"
        return f"Score : {self.score}"

    def start(self):
        self.snake = Snake(self.window, self.snake_obj)
        self.snake.spawn_food()
        self.is_lost = False
        self.is_frozen = True
        self.score = 0

    def listen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.changed:
            self.snake.direction = [-1, 0]
            self.changed = True
        if keys[pygame.K_RIGHT] and not self.changed:
            self.snake.direction = [1, 0]
            self.is_frozen = False
            self.changed = True
        if keys[pygame.K_UP] and not self.changed:
            self.snake.direction = [0, -1]
            self.is_frozen = False
            self.changed = True
        if keys[pygame.K_DOWN] and not self.changed:
            self.snake.direction = [0, 1]
            self.is_frozen = False
            self.changed = True
        if keys[pygame.K_n] and self.is_lost:
            self.end()
        if keys[pygame.K_y] and self.is_lost:
            self.start()
        if pygame.event.get(pygame.QUIT):
            self.end()

    def update(self):
        pygame.display.update()
        self.window.fill(self.bg_color)
        self.snake.draw_body()
        self.snake.draw_food()

    def levelup(self):
        self.score += 1
        self.snake.spawn_food()
        self.snake.grow()

    def lose(self):
        self.is_frozen = True
        self.is_lost = True

    def run(self):
        self.clock.tick(self.rate)
        self.write(self.text)
        self.changed = False
        self.listen()
        self.update()
        if self.snake.ate:
            self.levelup()
        if self.snake.crashed:
            self.lose()
        if not self.is_frozen:
            self.snake.move()

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
