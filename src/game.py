from src.frog import Frog
from src.bug import Bug
from src.obstacle import Obstacle
from src.utils import show_message_menu, show_difficulty_menu, draw_text
from src.constants import *


def game_loop(nickname, difficulty):
    pygame.init()
    frog = Frog()
    bugs = [Bug() for _ in range(difficulty)]
    obstacles = [Obstacle() for _ in range(5)]
    score = 0
    reached_end_count = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        frog.move(dx, dy, obstacles)

        # Перевірка зіткнення жабки з жуками
        for bug in bugs:
            if (frog.x < bug.x + bug_width and frog.x + frog_width > bug.x and
                    frog.y < bug.y + bug_height and frog.y + frog_height > bug.y):
                if frog.lose_life():
                    frog.reset()
                else:
                    show_message_menu("Програш!", main, pygame.quit)
                    return

        if frog.y == 0:
            score += 1
            reached_end_count += 1
            frog.reached_end()
            frog.reset()
            if reached_end_count % 10 == 0:
                bugs.extend([Bug() for _ in range(2)])
            if reached_end_count >= 20:
                show_message_menu(f"Вітаю! Гру завершено!", main, pygame.quit)
                return

        # Фон
        screen.blit(background, (0, 0))

        # Старт та фініш
        screen.blit(start, (0, screen_height - start.get_height()))
        screen.blit(finish, (0, 0))

        frog.draw()
        for bug in bugs:
            bug.draw()
            bug.update()
        for obstacle in obstacles:
            obstacle.draw()

        draw_text(f"Гравець: {nickname}", black, 10, 55)
        draw_text(f"Рахунок: {reached_end_count}", black, 10, 85)

        pygame.display.flip()
        clock.tick(fps)


def main():
    nickname = show_message_menu("Введіть свій нікнейм:", lambda: None, pygame.quit, input_nickname=True)
    difficulty = show_difficulty_menu()
    if difficulty != "exit":
        game_loop(nickname, difficulty)
    else:
        pygame.quit()
        exit()


main()
