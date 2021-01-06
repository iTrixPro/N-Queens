##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 06/01/2020
# descritpion: contains all the utilities functions needed by solving.py and nqueen.py
##########################################

def queenCanTattack(board, size, row, column):
  """Check if the new queen will not be able to attack an other one.

  Args:
      board (array): board on which the queen will be
      size (int): size of the board
      row (int): row position on the board
      column (int): column position on the board

  Returns:
      [boolean]: True, if unable to attack
  """

  can_t_attack = True

  # check cardinals
  for idx_row in range(size):
      if idx_row != row and board[idx_row][column] == 1:
          return not can_t_attack

  for idx_column in range(size):
      if idx_column != column and board[row][idx_column] == 1:
          return not can_t_attack

  # check diagonals
  for idx_row, idx_column in zip(range(row - 1, -1, -1), range(column + 1, size)):
      if board[idx_row][idx_column] == 1:
          return not can_t_attack

  for idx_row, idx_column in zip(range(row + 1, size), range(column + 1, size)):
      if board[idx_row][idx_column] == 1:
          return not can_t_attack

  for idx_row, idx_column in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
      if board[idx_row][idx_column] == 1:
          return not can_t_attack

  for idx_row, idx_column in zip(range(row + 1, size), range(column - 1, -1, -1)):
      if board[idx_row][idx_column] == 1:
          return not can_t_attack

  return can_t_attack

def isSafe(row, col, oblique, oblique_inv, ctrl_oblique, ctrl_obliqueinv):
  """[summary]

  Args:
      row ([type]): [description]
      col ([type]): [description]
      oblique ([type]): [description]
      oblique_inv ([type]): [description]
      ctrl_oblique ([type]): [description]
      ctrl_obliqueinv ([type]): [description]

  Returns:
      [type]: [description]
  """
  if ctrl_oblique[oblique[row][col]] or ctrl_obliqueinv[oblique_inv[row][col]] or ctrl_obliqueinv[row]:
      return False
  return True

def initCtrl(size):
  """Init...

  Args:
      size (int): size of the board

  Returns:
      [type]: [description]
  """
  x = 2 * size - 1
  ctrl_oblique = [False] * x
  ctrl_obliqueinv = [False] * x

  return ctrl_oblique, ctrl_obliqueinv

def initObliques(size):
  """Init...

  Args:
      size (int): size of the board

  Returns:
      [type]: [description]
  """
  oblique = generateArray(size)
  oblique_inv = generateArray(size)

  for row in range(size):
      for column in range(size):
          oblique[row][column] = row + column
          oblique_inv[row][column] = row - column + (size -1)

  return oblique, oblique_inv

def generateArray(size):
  """Return a 2D array full of 0.

  Args:
      size (int): number of row and number of column

  Returns:
      [array]: 2D array full of 0
  """

  return [[0 for x in range(size)] for y in range(size)]