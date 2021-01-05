##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# created: 28/12/2020
# modified: 05/01/2021
##########################################

from soluce.board import Board

def print_board(size, board):
  """Display the board.

  Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board
  """

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
  board = Board(board, size)
  return board.queensCanTattack()

def is_soluce(size, board):
  """Check solution has been found.

  Args:
      size (int): size of the board
      board (array): 2 dimensional array containing the content of the board
  """

  board = Board(board, size)
  is_soluce = True if board.getNumberOfQueen() == size else False

  if(is_soluce):
    is_soluce = board.queensCanTattack()

  return is_soluce, board.getNumberOfQueen()