##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 06/01/2020
# see: utils.py
# description: Contains the different algorithms used to resolve the N-Queen problem
##########################################

from soluce.utils import *

def backtracking(board, column, size):
    """Algo to solve the problem. Deprecated for a size superior at 20.

    Args:
        board (array)
        size (int): size of the board

    Returns:
        [array]: final board
        [boolean]: success to find a solution
    """

    if column == size:
        return board, True

    for row in range(size):
        if queenCanTattack(board, size, row, column):
            board[row][column] = 1
            board, solved = backtracking(board, column + 1, size)

            if solved:
                return board, solved

            board[row][column] = 0

    return board, False

def branchAndBound(board,
                   column,
                   size,
                   oblique,
                   oblique_inv,
                   ctrl_oblique,
                   ctrl_obliqueinv):
    """[summary]

    Args:
        board (array)
        column (int): number of queen, will be the column index
        size (int): size of the board
        oblique ([type]): [description]
        oblique_inv ([type]): [description]
        ctrl_oblique ([type]): [description]
        ctrl_obliqueinv ([type]): [description]

    Returns:
        [type]: [description]
    """

    if column >= size:
        return board, True

    for row in range(size):
        if isSafe(row, column, oblique, oblique_inv, ctrl_oblique, ctrl_obliqueinv):
            board[row][column] = 1
            ctrl_oblique[oblique[row][column]] = True
            ctrl_obliqueinv[oblique_inv[row][column]] = True

            board, solved = branchAndBound(board, column + 1, size, oblique, oblique_inv, ctrl_oblique, ctrl_obliqueinv)

            if solved:
                return board, solved

            board[row][column] = 0
            ctrl_oblique[oblique[row][column]] = False
            ctrl_obliqueinv[oblique_inv[row][column]] = False

    return board, False