# from soluce.solving import *


def print_board(taille, board):
    for i in range(taille):
        for j in range(taille):
            print(" " + str(board[i][j]), end='')
        print()


def addQueen(board, row, coll):
    if can_t_attack_checkRight(row, coll) is True and board[row][coll] != 1:
        board[row][coll] = 1


def can_t_attack(taille, board):
    for j in range(taille):
        for i in range(taille):
            if board[i][j] == 1 and can_t_attack_checkRight(board, j, i, taille) is False:
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
            if board[i][j] == 1 and can_t_attack_checkRight(board, j, i, taille) is False:
                print_board(taille, board)
                return False, nbQueen
    if nbQueen == taille:
        return True, nbQueen
    else:
        return False, nbQueen


def solve_n_queen_small(taille, board):
    pass


def solve_n_queen_big(taille, board):
    pass


def solve_n_queen_all_soluce(taille, board):
    pass


def can_t_attack_checkRight(board, col, row, taille):  # row and col from the queen's vew
    for i in range(row + 1, taille):
        if board[i][col] == 1:
            board[i][col] = 2
            return False
    for i in range(col + 1, taille):
        if board[row][i] == 1:
            board[i][col] = 2
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, taille)):
        if board[i][j] == 1:
            board[i][j] = 2
            return False
    for i, j in zip(range(row + 1, taille), range(col + 1, taille)):
        if board[i][j] == 1:
            board[i][j] = 2
            return False
    return True
