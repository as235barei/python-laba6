import random
from src.constants import *


class Bug:
    def __init__(self):
        self.x = random.randint(0, screen_width - bug_width)
        self.y = random.randint(
            finish_zone_height, screen_height - bug_height - frog_height)
        self.speed = random.randint(3, 7)
        self.direction = random.choice([-1, 1])

    def draw(self):
        screen.blit(bug_img, (self.x, self.y))

    def update(self):
        self.x += self.speed * self.direction
        if self.x < 0 or self.x > screen_width - bug_width:
            self.direction *= -1
