from random import choice

import pygame

from listf import words


def start_game():
    pygame.init()

    pygame.display.set_caption('Игра веселица!')
    screen = pygame.display.set_mode((700, 700))
    screen.fill((255, 255, 255))
    play_field_text(screen)
    flag_text = True
    pygame.display.update()

    walk_viselica = [
        pygame.image.load('images/viselone.png').convert_alpha(),
        pygame.image.load('images/viseltwo.png').convert_alpha(),
        pygame.image.load('images/viselthree.png').convert_alpha(),
        pygame.image.load('images/viselfour.png').convert_alpha(),
        pygame.image.load('images/viselfive.png').convert_alpha(),
        pygame.image.load('images/viselsix.png').convert_alpha(),
        pygame.image.load('images/viselseven.png').convert_alpha(),
    ]

    flag_count = 0
    flag_game_start = True
    running = True
    flag_restart_and_quit = False
    flag_restart_and_quit_lose = False

    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and flag_text:
                if 468 <= sum(event.pos) <= 535:
                    word = cursor_game_yes(screen)
                    flag_text = False
                elif 1001 <= sum(event.pos) <= 1087:
                    cursor_game_not(screen)

            elif event.type == pygame.MOUSEBUTTONDOWN and flag_game_start:
                len_word = ' _' * len(word)
                game_play(screen, flag_count, walk_viselica, len_word)
                flag_game_start = False
            elif event.type == pygame.KEYUP:
                event_key = chr(event.key)
                len_word, flag_count = inputkey(screen, word, len_word, event_key, walk_viselica, flag_count)

                flag_restart_and_quit = check_win(screen, len_word)
                flag_restart_and_quit_lose = check_lose(screen, flag_count, walk_viselica)

            elif (flag_restart_and_quit or flag_restart_and_quit_lose) and event.type == pygame.MOUSEBUTTONDOWN:
                if 606 < sum(event.pos) < 710:

                    return True

                elif 1129 < sum(event.pos) < 1205:
                    running = False
                    pygame.quit()


def inputkey(screen, word, len_word, evenkey, walk, count):
    if evenkey in len_word:
        return len_word, count
    flag = True
    num_index = 0
    for i in word:

        if evenkey == i:
            flag = False

            if num_index == 0:
                index = word.index(i)
                num_index += 1
            else:
                index = word.rfind(i)

            n = len_word.split(' ')

            if n[0] == '':
                n[0] = '_'

            n.pop(0)
            n[index] = evenkey

            len_word = ''

            for j in n:
                len_word += f' {j}'

    if flag:
        count += 1
        print(count)

    font = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
    font_s = font.render(len_word, True, 'Black')
    screen.blit(font_s, (10, 200))

    screen = pygame.display.set_mode((700, 700))
    screen.fill((255, 255, 255))

    screen.blit(walk[count], (20, 50))

    font = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
    font_s = font.render(len_word, True, 'Black')

    font_game_info = pygame.font.Font('fonts/Roboto-Black.ttf', 20)
    font_game_info_s = font_game_info.render('И так перед тобой виселица и пустые клетки', True, 'Black')
    font_game_info_a = font_game_info.render('Нажимая на клавиатуру ты выбираешь букву, если это буква есть, то', True,
                                             'Black')
    font_game_info_b = font_game_info.render('открывается клетка с нею иначе же дорисовывается часть тела', True,
                                             'Black')
    font_game_info_c = font_game_info.render('твоего игрока для виселицы', True, 'Black')

    screen.blit(font_s, (10, 200))
    screen.blit(font_game_info_s, (10, 400))
    screen.blit(font_game_info_a, (10, 430))
    screen.blit(font_game_info_b, (10, 460))
    screen.blit(font_game_info_c, (10, 490))

    return len_word, count


def check_win(screen, len_word):
    if '_' not in len_word:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)
        text_surface = font.render(len_word, True, 'Black')

        screen.blit(text_surface, (240, 200))

        font = pygame.font.Font('fonts/Roboto-Black.ttf', 33)
        text_surface = font.render('Поздравляю! Ты смог отгадать слово:', True, 'Black')

        screen.blit(text_surface, (50, 120))

        text_surface = font.render('Ты молодец, но следующий раз', True, 'Black')
        text_surface_end = font.render('я тебя точно повешу:)', True, 'Black')

        screen.blit(text_surface, (90, 350))
        screen.blit(text_surface_end, (170, 400))

        font_restart = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
        surface_font_restart = font_restart.render('restart', True, 'Green')

        font_quit = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
        surface_font_quit = font_quit.render('quit', True, 'Red')

        screen.blit(surface_font_restart, (50, 550))
        screen.blit(surface_font_quit, (575, 550))

        return True
    else:
        return False


def check_lose(screen, count, walk):
    if count == 6:
        screen.fill((255, 255, 255))
        screen.blit(walk[count], (300, 50))
        font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)
        text_surface = font.render('Ха-ха тебя повесили!', True, 'Black')

        screen.blit(text_surface, (80, 300))

        font_restart = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
        surface_font_restart = font_restart.render('restart', True, 'Green')

        font_quit = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
        surface_font_quit = font_quit.render('quit', True, 'Red')

        screen.blit(surface_font_restart, (50, 550))
        screen.blit(surface_font_quit, (575, 550))

        return True
    return False


def play_field_text(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
    text_surface = font.render('Привет желаешь сыграть в виселицу?', True, 'black')

    font_yes = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
    text_surface_yes = font_yes.render('Да', True, 'black')

    font_no = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
    text_surface_no = font_no.render('Нет', True, 'black')

    screen.blit(text_surface, (80, 70))
    screen.blit(text_surface_yes, (65, 400))
    screen.blit(text_surface_no, (600, 400))


def cursor_game_yes(screen):
    screen.fill((255, 255, 255))
    font_game_on = pygame.font.Font('fonts/Roboto-Black.ttf', 35)
    text_surface = font_game_on.render('Отлично, тогда начинаем!', True, 'Black')

    font_text_mini = pygame.font.Font('fonts/Roboto-Black.ttf', 13)
    text_surface_mini = font_text_mini.render('Кликни мышью по любой части экрана', True, 'Black')

    screen.blit(text_surface, (130, 300))
    screen.blit(text_surface_mini, (450, 600))

    return choice(words)


def cursor_game_not(screen):
    font_game_off = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
    text_surface = font_game_off.render('Приходи еще, буду рад тебя повесить :)', True, 'Black')
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (65, 300))


def game_play(screen, count, walk, len_word):
    screen = pygame.display.set_mode((700, 700))
    screen.fill((255, 255, 255))

    screen.blit(walk[count], (20, 50))

    font = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
    font_s = font.render(len_word, True, 'Black')

    font_game_info = pygame.font.Font('fonts/Roboto-Black.ttf', 20)
    font_game_info_s = font_game_info.render('И так перед тобой виселица и пустые клетки', True, 'Black')
    font_game_info_a = font_game_info.render('Нажимая на клавиатуру ты выбираешь букву, если это буква есть, то', True,
                                             'Black')
    font_game_info_b = font_game_info.render('открывается клетка с нею иначе же дорисовывается часть тела', True,
                                             'Black')
    font_game_info_c = font_game_info.render('твоего игрока для виселицы', True, 'Black')

    screen.blit(font_s, (10, 200))
    screen.blit(font_game_info_s, (10, 400))
    screen.blit(font_game_info_a, (10, 430))
    screen.blit(font_game_info_b, (10, 460))
    screen.blit(font_game_info_c, (10, 490))


def main():
    flag = True
    while flag:
        flag = start_game()


if __name__ == '__main__':
    main()
