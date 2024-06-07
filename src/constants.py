import pygame

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Назва вікна
pygame.display.set_caption("Frog")

# Зображення та кольори
frog_images = [pygame.image.load(
    f'./assets/images/frog/frog{i+1}.png') for i in range(7)]
bug_img = pygame.image.load('./assets/images/bug.png')
obstacle_img = pygame.image.load('./assets/images/obstacle.png')
heart_img = pygame.image.load('./assets/images/heart.png')
start = pygame.image.load('./assets/images/grass-start.png')
finish = pygame.image.load('./assets/images/finish.png')
background = pygame.image.load('./assets/images/background.png')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
rose = (255, 182, 193)

# Розміри об'єктів
frog_width = 50
frog_height = 50
bug_width = 30
bug_height = 30
obstacle_width = 100
obstacle_height = 20
heart_width = 30
heart_height = 30

# Кількість життів жабки
max_lives = 3

# Шрифт меню
font = pygame.font.Font(None, 36)

# Висота зони фінішу
finish_zone_height = finish.get_height()

# Швидкість гри
fps = 30
