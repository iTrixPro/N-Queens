def print_board(taille, board):
    for i in range(taille):
        for j in range(taille):
            print(board[i][j], end='')
        print()


def addQueen(board, row, coll):
    if isSafe(row, coll) is True and board[row][coll] != 1:
        board[row][coll] = 1


def isSafe(board, row, col, taille):  # row and col from the queen's vew
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i in range(col + 1, taille):
        if board[row][i] == 1:
            return False
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i in range(row + 1, taille):
        if board[i][col] == 1:
            return False
    for i in range(row, 0, -1):
        for j in range(col, 0, -1):
            if board[i][j] == 1:
                return False
    for i in range(row, 0, -1):
        for j in range(col, taille, +1):
            if board[i][j] == 1:
                return False
    for i in range(row, taille, +1):
        for j in range(col, taille, +1):
            if board[i][j] == 1:
                return False
    for i in range(row, taille, +1):
        for j in range(col, 0, -1):
            if board[i][j] == 1:
                return False
