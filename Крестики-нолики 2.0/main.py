from random import choice

import pygame

import move_cell
import pk_field_motion
from data import check_numbers


def start_game(board):
    flag_text = True
    flag_muoshedown = True

    count = 0

    pygame.init()

    pygame.display.set_caption('Крестики-нолики')
    screen = pygame.display.set_mode((1000, 1000))
    play_field_text(screen)
    running = True
    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and flag_text:
                if 150 < event.pos[0] < 210 and 690 < event.pos[1] < 753:
                    play_field(screen)
                    player, pk = 'X', 'O'
                    one_playing = choice([player, pk])

                    flag_text = False
                    if one_playing == pk:
                        pk_move(screen, pk, player, board)
                        count += 1
                elif 806 < event.pos[0] < 855 and 694 < event.pos[1] < 745:
                    play_field(screen)
                    player = 'O'
                    pk = 'X'
                    one_playing = choice([player, pk])
                    if one_playing == pk:
                        pk_move(screen, pk, player, board)
                        count += 1
                    flag_text = False

            elif event.type == pygame.MOUSEBUTTONDOWN and flag_muoshedown:
                flg = player_move(screen, player, event.pos, board)
                if flg:
                    continue
                count += 1

                if count > 4:
                    for num in check_numbers:
                        if board[num[0]] == board[num[1]] == board[num[2]] == player:
                            count = 0
                            play_game_win(screen)
                            flag_muoshedown = False
                        elif board[num[0]] == board[num[1]] == board[num[2]] == pk:
                            count = 0
                            play_game_lose(screen)
                            flag_muoshedown = False

                if count != 0:
                    pk_move(screen, pk, player, board)
                    count += 1

                    if count > 4:
                        for num in check_numbers:
                            if board[num[0]] == board[num[1]] == board[num[2]] == player:
                                count = 0
                                play_game_win(screen)
                                flag_muoshedown = False
                            elif board[num[0]] == board[num[1]] == board[num[2]] == pk:
                                count = 0
                                play_game_lose(screen)
                                flag_muoshedown = False
                if count >= 9:
                    flag_muoshedown = False
                    play_game_draw(screen)
                    count = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 120 < event.pos[0] < 273 and 867 < event.pos[1] < 895:
                    return True
                elif 775 < event.pos[0] < 860 and 863 < event.pos[1] < 894:
                    pygame.init()
                    return False


def player_move(screen, player, pos, board):
    if pos[0] < 325 and pos[1] < 325 and board[1] == '1':
        move_cell.move_one(screen, player)
        board[1] = player
        return False
    elif 338 < pos[0] < 666 and pos[1] < 315 and board[2] == '2':
        move_cell.move_two(screen, player)
        board[2] = player
        return False
    elif 688 < pos[0] < 996 and pos[1] < 315 and board[3] == '3':
        move_cell.move_three(screen, player)
        board[3] = player
        return False
    elif pos[0] < 315 and 337 < pos[1] < 666 and board[4] == '4':
        move_cell.move_four(screen, player)
        board[4] = player
        return False
    elif 336 < pos[0] < 664 and 335 < pos[1] < 663 and board[5] == '5':
        move_cell.move_five(screen, player)
        board[5] = player
        return False
    elif 685 < pos[0] < 1000 and 338 < pos[1] < 665 and board[6] == '6':
        move_cell.move_six(screen, player)
        board[6] = player
        return False
    elif pos[0] < 315 and 668 < pos[1] and board[7] == '7':
        move_cell.move_seven(screen, player)
        board[7] = player
        return False
    elif 335 < pos[0] < 665 and 687 < pos[1] and board[8] == '8':
        move_cell.move_eight(screen, player)
        board[8] = player
        return False
    elif 668 < pos[0] and 668 < pos[1] and board[9] == '9':
        move_cell.move_nine(screen, player)
        board[9] = player
        return False
    else:
        return True


def pk_move(screen, pk, player, board):
    if pk_field_motion.one_motion(pk, screen, board):
        pass
    elif pk_field_motion.two_motion(pk, player, screen, board):
        pass
    elif pk_field_motion.three_motion(pk, screen, board):
        pass
    elif pk_field_motion.four_motion(pk, screen, board):
        pass
    else:
        pk_field_motion.five_motion(pk, screen, board)


def play_field(screen):
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, 'black', [0, 325], [1000, 325], width=20)
    pygame.draw.line(screen, 'black', [0, 675], [1000, 675], width=20)
    pygame.draw.line(screen, 'black', [325, 0], [325, 1000], width=20)
    pygame.draw.line(screen, 'black', [675, 0], [675, 1000], width=20)

    pygame.display.update()


def play_game_win(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)
    font_surface = font.render(f'Поздавляю ты одержал победу!', True, 'black')
    font_surface_restart = font.render(f'Желаешь сыграть снова?', True, 'black')

    screen.blit(font_surface_restart, (160, 500))
    screen.blit(font_surface, (100, 450))

    restart_and_quit(screen)


def play_game_lose(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)
    font_surface = font.render(f'Ты проиграл!:(', True, 'Black')

    screen.blit(font_surface, (325, 470))

    restart_and_quit(screen)


def play_game_draw(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('fonts/Roboto-Black.ttf', (50))
    font_surface = font.render('Ничья!', True, 'Black')

    screen.blit(font_surface, (410, 470))

    restart_and_quit(screen)


def restart_and_quit(screen):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)

    font_restart_surface = font.render('restart', True, 'Green')
    font_exit_surface = font.render('exit', True, 'Red')

    screen.blit(font_restart_surface, (120, 850))
    screen.blit(font_exit_surface, (775, 850))


def play_field_text(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 50)
    text_surface = font.render('Привет, выбери чем будешь играть', True, 'Black')

    font_x = pygame.font.Font('fonts/Roboto-Black.ttf', 90)
    text_surface_x = font_x.render('X', True, 'Black')

    font_y = pygame.font.Font('fonts/Roboto-Black.ttf', 90)
    text_surface_y = font_y.render('O', True, 'Black')

    screen.blit(text_surface, (85, 180))
    screen.blit(text_surface_x, (150, 670))
    screen.blit(text_surface_y, (800, 670))
    pygame.display.update()


def game():
    while True:
        board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flag = start_game(board)
        if not flag:
            break


if __name__ == '__main__':
    game()
