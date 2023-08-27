import pygame
import math

class Prey:
    def __init__(self, x, y, control_keys):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.control_keys = control_keys

    def draw(self, window):
        pygame.draw.rect(window, (0, 100, 0), (self.x, self.y, self.width, self.height))

    def move(self, keys_pressed):
        dx = 0
        dy = 0
        speed = 0.1

        if keys_pressed[self.control_keys['left']] and self.x > 0:
            dx -= speed
        if keys_pressed[self.control_keys['right']] and self.x < 1000 - self.width:
            dx += speed
        if keys_pressed[self.control_keys['up']] and self.y > 0:
            dy -= speed
        if keys_pressed[self.control_keys['down']] and self.y < 1000 - self.height:
            dy += speed

        if dx != 0 and dy != 0:
            length = math.sqrt(dx ** 2 + dy ** 2)
            dx = dx / length * speed
            dy = dy / length * speed

        self.x += dx
        self.y += dy


class Predator:
    def __init__(self, x, y, control_keys):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.control_keys = control_keys

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # color red = (255, 0, 0)

    def move(self, keys_pressed):
        dx = 0
        dy = 0

        speed = 0.1

        if keys_pressed[self.control_keys['left']] and self.x > 0:
            dx -= speed
        if keys_pressed[self.control_keys['right']] and self.x < 1000 - self.width:
            dx += speed
        if keys_pressed[self.control_keys['up']] and self.y > 0:
            dy -= speed
        if keys_pressed[self.control_keys['down']] and self.y < 1000 - self.height:
            dy += speed

        if dx != 0 and dy != 0:
            length = math.sqrt(dx ** 2 + dy ** 2)
            dx = dx / length * speed
            dy = dy / length * speed

        self.x += dx
        self.y += dy