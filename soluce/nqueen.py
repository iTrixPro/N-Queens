##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 05/01/2021
# see: board.py, solving.py
# description: main file,
# contains all the main functions needed for the N-Queen problem
##########################################

from soluce.board import Board
from soluce.solving import (
  backtracking, branchAndBound, backtrackingAllSoluce
)
from soluce.utils import (
  initObliques, initCtrl
)


def print_board(size, board):
    """Display the board.

    Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board
    """

    if not isinstance(board, Board):
        board = Board(board, size)

    print(board)


def can_t_attack(size, board):
    """Check that none of the queens can attack each others.

    Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board

    Returns:
      [boolean]: True, if none of them can attack
    """

    if not isinstance(board, Board):
        board = Board(board, size)

    return board.queensCanTattack()


def is_soluce(size, board):
    """Check solution has been found.

    Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board
    """

    if not isinstance(board, Board):
        board = Board(board, size)

    is_soluce = True if board.getNumberOfQueen() == size else False

    if(is_soluce):
        is_soluce = board.queensCanTattack()

    return is_soluce, board.getNumberOfQueen()


def solve_n_queen_small(size, board):
    """Solve the problem for a small board.

    Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board

    Returns:
      [array]: final board
      [boolean]: success or not
    """

    return backtracking(board, 0, size)


def solve_n_queen_big(size, board):

    oblique, oblique_inv = initObliques(size)
    ctrl_line, ctrl_oblique, ctrl_obliqueinv = initCtrl(size)

    return branchAndBound(board, 0, size, oblique, oblique_inv,
                          ctrl_line, ctrl_oblique, ctrl_obliqueinv)


def solve_n_queen_all_soluce(size, board):
    boards = []
    boards = backtrackingAllSoluce(board, 0, size, boards)
    return boards
