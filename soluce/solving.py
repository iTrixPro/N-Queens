
def backtrack(board, col, taille):
    if col >= taille:
        return True

    for i in range(taille):

        if can_t_attack_check(board, i, col, taille) is True:
            board[i][col] = 1
            if backtrack(board, col + 1, taille) is True:
                return True
            print_board_debug(taille, board)
            board[i][col] = 0
            print_board_debug(taille, board)
    return False


def addQueen(board, row, coll):
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
            # board[i][j] = 2
            return False
    return True


def print_board_debug(taille, board):
    for i in range(taille):
        for j in range(taille):
            print(" " + str(board[i][j]), end='')
        print()
