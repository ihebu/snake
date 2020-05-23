import random

import pygame


class Snake:
    def __init__(self, window, obj):
        self.color = obj["color"]
        self.width = obj["width"]
        self.length = obj["length"]
        self.window = window
        self.screen_height = window.get_height()
        self.screen_width = window.get_width()
        # x[0] and y[0] head of the snake
        self.x = [self.width * i for i in range(5 + self.length, 5, -1)]
        self.y = [self.width * ((self.screen_height // self.width) // 2)] * self.length
        # initialise direction to right
        self._direction = [1, 0]
        self.food = [None, None]

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if self._direction != [-x for x in value]:
            self._direction = value

    def draw_body(self):
        for i in range(self.length):
            rect = (self.x[i], self.y[i], self.width, self.width)
            pygame.draw.rect(self.window, self.color, rect)

    def grow(self):
        self.length += 1
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
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        # updating the head
        self.x[0] += self.direction[0] * self.width
        self.y[0] += self.direction[1] * self.width

    @property
    def ate(self):
        return (self.x[0], self.y[0]) == self.food

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

    def spawn_food(self):
        # the food cordinates should be a multiple of the snake width
        # and it should not appear randomly in a space taken by the snake body
        x = set(i * self.width for i in range(self.screen_width // self.width))
        x = tuple(x - set(self.x))
        y = set(i * self.width for i in range(self.screen_height // self.width))
        y = tuple(y - set(self.y))
        self.food = random.choice(x), random.choice(y)

    def draw_food(self):
        x, y = self.food
        rect = (x, y, self.width, self.width)
        pygame.draw.rect(self.window, self.color, rect)
