from soluce.solving import *


def print_board(taille, board):
    for i in range(taille):
        for j in range(taille):
            print(" " + str(board[i][j]), end='')
        print()


def can_t_attack(taille, board):
    for j in range(taille):
        for i in range(taille):
            if board[i][j] == 1 and can_t_attack_check(board, j, i, taille) is False:
                print_board(taille, board)
                return False

    return True


def is_soluce(taille, board):
    nbQueen = 0
    for i in range(taille):
        for j in range(taille):
            if board[i][j] == 1:
                nbQueen += 1
    for j in range(taille):
        for i in range(taille):
            if board[i][j] == 1 and can_t_attack_check(board, j, i, taille) is False:
                print_board(taille, board)
                return False, nbQueen
    if nbQueen == taille:
        return True, nbQueen
    else:
        return False, nbQueen


def solve_n_queen_small(taille, board):
    rep, board = backtrack(board, 0, taille)
    return board, rep


def solve_n_queen_big(taille, board):
    pass


def solve_n_queen_all_soluce(taille, board):
    pass


