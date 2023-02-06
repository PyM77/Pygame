import pygame.display



def move_one(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (40, -40))


def move_two(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (400, -40))


def move_three(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (730, -40))


def move_four(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (40, 300))


def move_five(screen, lt):
    # global board
    # if board[5] != 5:
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (400, 300))


def move_six(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (730, 300))


def move_seven(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (40, 650))


def move_eight(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (400, 650))


def move_nine(screen, lt):
    font = pygame.font.Font('fonts/Roboto-Black.ttf', 350)
    text_font = font.render(lt, True, 'Black')

    screen.blit(text_font, (730, 650))


def move_num(num, screen, lt, board):
    if num == 1 and board[1] == '1':
        move_one(screen, lt)
        board[1] = lt
        # flag_move['one'] = False
    elif num == 2 and board[2] == '2':
        move_two(screen, lt)
        board[2] = lt
    elif num == 3 and board[3] == '3':
        move_three(screen, lt)
        board[3] = lt
    elif num == 4 and board[4] == '4':
        move_four(screen, lt)
        board[4] = lt
    elif num == 5 and board[5] == '5':
        move_five(screen, lt)
        board[5] = lt
    elif num == 6 and board[6] == '6':
        move_six(screen, lt)
        board[6] = lt
    elif num == 7 and board[7] == '7':
        move_seven(screen, lt)
        board[7] = lt
    elif num == 8 and board[8] == '8':
        move_eight(screen, lt)
        board[8] = lt
    elif num == 9 and board[9] == '9':
        move_nine(screen, lt)
        board[9] = lt
    # print(board)
