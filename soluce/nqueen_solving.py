
class Jeu:  # Class defining the bord & rules

    def __init__(self, board):
        self.board = board
        self.taille = len(self.board[0])

    def printBord(self):
        for i in range(self.taille):
            for j in range(self.taille):
                print(self.board[i][j], end='')
            print()

    def addQueen(self, row, coll):
        if self.isSafe(row, coll) is True and self.board[row][coll] != 1:
            self.board[row][coll] = 1

    def isSafe(self, row, col):  # row and col from the queen's vew
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i in range(col + 1, self.taille):
            if self.board[row][i] == 1:
                return False
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        for i in range(row + 1, self.taille):
            if self.board[i][col] == 1:
                return False
        for i in range(row, 0, -1):
            for j in range(col, 0, -1):
                if self.board[i][j] == 1:
                    return False
        for i in range(row, 0, -1):
            for j in range(col, self.taille, +1):
                if self.board[i][j] == 1:
                    return False
        for i in range(row, self.taille, +1):
            for j in range(col, self.taille, +1):
                if self.board[i][j] == 1:
                    return False
        for i in range(row, self.taille, +1):
            for j in range(col, 0, -1):
                if self.board[i][j] == 1:
                    return False
