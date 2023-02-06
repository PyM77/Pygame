from random import choice

import move_cell
from data import *

def one_motion(lt_pk, screen, board):
    for num in check_numbers:
        if board[num[0]] == board[num[1]] == lt_pk and board[num[2]] == str(num[2]):
            # board[num[2]] = lt_pk
            move_cell.move_num(num[2], screen, lt_pk, board)
            return True
        elif board[num[1]] == board[num[2]] == lt_pk and board[num[0]] == str(num[0]):
            # board[num[0]] = lt_pk
            move_cell.move_num(num[0], screen, lt_pk, board)
            return True
        elif board[num[0]] == board[num[2]] == lt_pk and board[num[1]] == str(num[1]):
            # board[num[1]] = lt_pk
            move_cell.move_num(num[1], screen, lt_pk, board)
            return True
    return False


def two_motion(lt_pk, lt_player, screen, board):
    for num in check_numbers:
        if board[num[0]] == board[num[1]] == lt_player and board[num[2]] == str(num[2]):
            # board[num[2]] = lt_pk
            move_cell.move_num(num[2], screen, lt_pk, board)
            return True
        elif board[num[1]] == board[num[2]] == lt_player and board[num[0]] == str(num[0]):
            # board[num[0]] = lt_pk
            move_cell.move_num(num[0], screen, lt_pk, board)
            return True
        elif board[num[0]] == board[num[2]] == lt_player and board[num[1]] == str(num[1]):
            # board[num[1]] = lt_pk
            move_cell.move_num(num[1], screen, lt_pk, board)
            return True
    return False


def three_motion(lt_pk, screen, board):
    for i in cor_num:
        if board[i] == str(i):
            while True:
                n = choice(cor_num)
                if str(n) in board:
                    # board[n] = lt_pk
                    move_cell.move_num(n, screen, lt_pk, board)
                    return True

    else:
        # print('Все')
        return False


def four_motion(lt_pk, screen, board):
    if board[5] == '5':
        # board[5] = lt_pk
        move_cell.move_num(5, screen, lt_pk)
        return True
    return False


def five_motion(lt_pk, screen, board):
    for i in later_num:
        if board[i] == str(i):
            while True:
                n = choice(later_num)
                if str(n) in board:
                    # board[n] = lt_pk
                    move_cell.move_num(n, screen, lt_pk, board)
                    return True

    else:
        # print('Все')
        return False
