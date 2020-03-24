import random


class Snake(object):
    def __init__(self, window, color, width):
        self.width = width
        self.color = color
        self.window = window
        self.screen_height = window.get_height()
        self.screen_width = window.get_width()
        # original cordinates of the squares forming the snake
        self.x = [self.width * i for i in range(10, 5, -1)]
        self.y = [self.width * ((self.screen_height // self.width) // 2)] * 10
        # x[0] and y[0] head of the snake
        # initialise direction to right
        self.direction = [1, 0]
        self.food = [None, None]
        self.spawn_food()

    def draw_body(self, draw):
        for i in range(len(self.x)):
            draw.rect(
                self.window, self.color, (self.x[i], self.y[i], self.width, self.width)
            )

    def grow(self):
        # increase the snake size by 1 unit
        # check in which direction to add 1 unit to the snake
        if self.x[-1] == self.x[-2]:
            self.x.append(self.x[-1])
            self.y.append(2 * self.y[-1] - self.y[-2])

        else:
            self.y.append(self.y[-1])
            self.x.append(2 * self.x[-1] - self.x[-2])

    def move(self):
        # updating the body
        # each part of the snake takes the previous position of the one in front of it
        for i in range(len(self.x) - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        # updating the head
        self.x[0] += self.direction[0] * self.width
        self.y[0] += self.direction[1] * self.width

    @property
    def crashed(self):
        # check if the snake collides with itself
        if (self.x[0], self.y[0]) in zip(self.x[1:], self.y[1:]):
            return True
        # check if the snake collides with the wall
        if not 0 <= self.x[0] < self.screen_width:
            return True
        if not 0 <= self.y[0] < self.screen_height:
            return True
        # otherwise return False
        return False

    @property
    def ate(self):
        return (self.x[0], self.y[0]) == (self.food[0], self.food[1])

    def spawn_food(self):
        # the food cordinates should be a multiple of the snake width
        # and it should not appear randomly in a space taken by the snake body
        x = set(i * self.width for i in range(self.screen_width // self.width))
        x = tuple(x - set(self.x))
        y = set(i * self.width for i in range(self.screen_height // self.width))
        y = tuple(y - set(self.y))
        self.food = random.choice(x), random.choice(y)

    def draw_food(self, draw):
        x, y = self.food
        draw.rect(self.window, self.color, (x, y, self.width, self.width))
