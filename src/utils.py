from src.constants import *


def draw_text(text, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))


def show_message_menu(message, callback, exit_callback, input_nickname=False):
    clock = pygame.time.Clock()
    user_input = ""

    input_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2, 300, 50)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray12')
    active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_callback()
            elif event.type == pygame.KEYDOWN:
                if input_nickname:
                    if event.key == pygame.K_RETURN:
                        return user_input
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
                    if len(user_input) > 0:
                        active = True
                    else:
                        active = False
                else:
                    if event.key == pygame.K_RETURN:
                        callback()
                        return

        screen.fill(rose)
        draw_text(message, pygame.Color('purple'), screen_width // 3, screen_height // 2 - 50)

        if input_nickname:
            pygame.draw.rect(screen, color_passive if not active else color_active, input_rect, 2)
            text_surface = font.render(user_input, True, black)
            width = max(200, text_surface.get_width())
            height = text_surface.get_height()
            screen.blit(
                text_surface,
                (input_rect.x + (input_rect.width - width) // 2,
                 input_rect.y + (input_rect.height - height) // 2)
            )

        pygame.display.flip()
        clock.tick(fps)


def show_difficulty_menu():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and
                        screen_height // 2 - 50 < mouse_y < screen_height // 2):
                    return 3  # Легкий рівень
                elif (screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and
                      screen_height // 2 < mouse_y < screen_height // 2 + 50):
                    return 10  # Середній рівень
                elif (screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and
                      screen_height // 2 + 50 < mouse_y < screen_height // 2 + 100):
                    return 15  # Важкий рівень
                elif (screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and
                      screen_height // 2 + 100 < mouse_y < screen_height // 2 + 200):  # Вибір виходу
                    pygame.quit()
                    exit()

        screen.fill(rose)
        draw_text("Оберіть рівень складності:", pygame.Color('purple'), screen_width // 2 - 150,
                  screen_height // 2 - 100)
        draw_text("Легкий", pygame.Color('yellow'), screen_width // 2 - 100, screen_height // 2 - 50)
        draw_text("Середній", pygame.Color('darkorange'), screen_width // 2 - 100, screen_height // 2)
        draw_text("Важкий", pygame.Color('red'), screen_width // 2 - 100, screen_height // 2 + 50)
        draw_text("Вихід", black, screen_width // 2 - 100, screen_height // 2 + 100)

        pygame.display.flip()
        clock.tick(fps)
