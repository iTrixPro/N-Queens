"""################################################## beginning First solution"""


def backtrack(board, col, taille):
    if col == taille:
        return True, board

    for i in range(taille):

        if can_t_attack_check(board, col, i, taille) is True:
            board[i][col] = 1
            rep, board = backtrack(board, col + 1, taille)
            if rep is True:
                return True, board
            board[i][col] = 0
    return False, board


def addQueen(board, row, coll):  # Not sure if it's useful
    if can_t_attack_check(row, coll) is True and board[row][coll] != 1:
        board[row][coll] = 1
        return True
    return False


def can_t_attack_check(board, col, row, taille):  # row and col from the queen's pov
    for i in range(row + 1, taille):
        if board[i][col] == 1:
            # board[i][col] = 2
            return False
    for i in range(col + 1, taille):
        if board[row][i] == 1:
            # board[i][col] = 2
            return False
    for i in range(row - 1, -1, -1):
        if board[i][col] == 1:
            return False
    for i in range(col - 1, -1, -1):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, taille)):
        if board[i][j] == 1:
            # board[i][j] = 2
            return False
    for i, j in zip(range(row + 1, taille), range(col + 1, taille)):
        if board[i][j] == 1:
            # board[i][j] = 2
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            # board[i][j] = 2
            return False
    for i, j in zip(range(row + 1, taille), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            # board[i][j] = 2 (Tu peux enlever ces commentaire avec les égal 2)
            return False
    return True


def print_board_debug(taille, board):
    for i in range(taille):
        for j in range(taille):
            print(" " + str(board[i][j]), end='')
        print()


"""################################################## End of First solution"""
"""################################################## beginning of second solution"""


def branchAndBound():  # Le but est d'utiliser des matrices de booléens pour déterminer quels sens sont bloqués
    pass


def isSafe():
    pass


def generate_Array_Helpers(size):
    return [[0 for x in range(size)] for y in range(size)]


def initialize_helpers(taille):
    oblique = generate_Array_Helpers(taille)
    obliqueInv = generate_Array_Helpers(taille)
    ctrlLigne = [False] * taille
    x = 2 * taille - 1
    ctrlOblique = [False] * x
    ctrlObliqueInv = [False] * x
    for row in range(taille):
        for col in range(taille):
            oblique[row][col] = row + col
            obliqueInv[row][col] = row - col + (taille-1)
    return oblique, obliqueInv, ctrlLigne, ctrlOblique, ctrlObliqueInv
