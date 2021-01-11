##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 11/01/2020
# see: utils.py
# description: Contains the different algorithms used
# to resolve the N-Queen problem
##########################################

from soluce.utils import (
    queenCanTattack, isSafe
)


def backtracking(board, column, size):
    """Algo to solve the problem. Deprecated for a size superior at 20.

    Args:
        board (array)
        column (int) : equal to the number of queen
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
                   ctrl_line,
                   ctrl_oblique,
                   ctrl_obliqueinv):
    """Best algo to resolve the N-Queens problem (with N > 20)

    Args:
        board (array)
        column (int): number of queen, will be the column index
        size (int): size of the board
        oblique (array): for the diagionales
        oblique_inv (array): for the diagionales
        ctrl_line (array): for the rows
        ctrl_oblique (array): for the diagionales
        ctrl_obliqueinv (array): for the diagionales

    Returns:
        [array]: final content of the board
        [boolean] : success to solved the problem
    """

    if column >= size:
        return board, True

    for row in range(size):
        if isSafe(row, column, oblique, oblique_inv,
                  ctrl_line, ctrl_oblique, ctrl_obliqueinv):
            board[row][column] = 1
            ctrl_line[row] = True
            ctrl_oblique[oblique[row][column]] = True
            ctrl_obliqueinv[oblique_inv[row][column]] = True

            board, solved = branchAndBound(board, column + 1, size,
                                           oblique, oblique_inv,
                                           ctrl_line, ctrl_oblique,
                                           ctrl_obliqueinv)

            if solved:
                return board, solved

            board[row][column] = 0
            ctrl_line[row] = True
            ctrl_oblique[oblique[row][column]] = False
            ctrl_obliqueinv[oblique_inv[row][column]] = False

    return board, False


def backtrackingAllSoluce(board, column, size, boards):
    """Give all the soluce of the N-Queens problem using the backtracking algo.

    Args:
        board (array): content of the board
        column (int): equal to the number of queen
        size (int): size of the board
        boards (array): result, all the solution

    Returns:
        [array]: boards, all the soluce
    """

    if column == size:
        return boards

    for row in range(size):
        if queenCanTattack(board, size, row, column) is True:
            board[row][column] = 1
            boards = backtrackingAllSoluce(board, column + 1, size, boards)
            board[row][column] = 0

    return boards


def branchAndBoundAllSoluce(board,
                            column,
                            size,
                            oblique,
                            oblique_inv,
                            ctrl_line,
                            ctrl_oblique,
                            ctrl_obliqueinv,
                            boards):
    """Give all the soluce of the N-Queens problem using the branchAndBound algo.

    Args:
        board (array)
        column (int): number of queen, will be the column index
        size (int): size of the board
        oblique (array): for the diagionales
        oblique_inv (array): for the diagionales
        ctrl_line (array): for the rows
        ctrl_oblique (array): for the diagionales
        ctrl_obliqueinv (array): for the diagionales
        boards (array): all the soluce
    """

    if column >= size:
        return boards

    for row in range(size):
        if isSafe(row, column, oblique, oblique_inv,
                  ctrl_line, ctrl_oblique, ctrl_obliqueinv):
            board[row][column] = 1
            ctrl_line[row] = True
            ctrl_oblique[oblique[row][column]] = True
            ctrl_obliqueinv[oblique_inv[row][column]] = True
            boards = branchAndBoundAllSoluce(board, column + 1, size,
                                             oblique, oblique_inv,
                                             ctrl_line, ctrl_oblique,
                                             ctrl_obliqueinv, boards)
            board[row][column] = 0
            ctrl_line[row] = False
            ctrl_oblique[oblique[row][column]] = False
            ctrl_obliqueinv[oblique_inv[row][column]] = False

    return boards
