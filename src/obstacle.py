import random
import pygame
from src.constants import *


class Obstacle:
    def __init__(self):
        self.x = random.randint(0, screen_width - obstacle_width)
        self.y = random.randint(
            finish_zone_height, (screen_height - obstacle_height - frog_height))

    def draw(self):
        screen.blit(obstacle_img, (self.x, self.y))
