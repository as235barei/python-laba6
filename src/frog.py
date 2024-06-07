from src.constants import *


class Frog:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height - frog_height
        self.speed = 15
        self.lives = max_lives
        self.reached_end_count = 0
        self.image_index = 0

    def draw(self):
        screen.blit(frog_images[self.image_index], (self.x, self.y))
        for i in range(self.lives):
            screen.blit(heart_img, (10 + i * (heart_width + 10), 10))

    def move(self, dx, dy, obstacles):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        # Обмеження руху жабки в межах екрана
        if new_x < 0:
            new_x = 0
        if new_x > screen_width - frog_width:
            new_x = screen_width - frog_width
        if new_y < 0:
            new_y = 0
        if new_y > screen_height - frog_height:
            new_y = screen_height - frog_height

        # Перевірка зіткнень з перешкодами
        for obstacle in obstacles:
            if (new_x < obstacle.x + obstacle_width and
                    new_x + frog_width > obstacle.x and
                    new_y < obstacle.y + obstacle_height and
                    new_y + frog_height > obstacle.y):
                return

        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = screen_width // 2
        self.y = screen_height - frog_height

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            return False
        else:
            return True

    def reached_end(self):
        self.reached_end_count += 1
        if self.reached_end_count % 3 == 0:
            self.image_index = (self.image_index + 1) % len(frog_images)
