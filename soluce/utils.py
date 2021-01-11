##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 06/01/2020
# descritpion: contains all the utilities functions
# needed by solving.py and nqueen.py
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
    for idx_row, idx_column in zip(range(row - 1, -1, -1),
                                   range(column + 1, size)):
        if board[idx_row][idx_column] == 1:
            return not can_t_attack

    for idx_row, idx_column in zip(range(row + 1, size),
                                   range(column + 1, size)):
        if board[idx_row][idx_column] == 1:
            return not can_t_attack

    for idx_row, idx_column in zip(range(row - 1, -1, -1),
                                   range(column - 1, -1, -1)):
        if board[idx_row][idx_column] == 1:
            return not can_t_attack

    for idx_row, idx_column in zip(range(row + 1, size),
                                   range(column - 1, -1, -1)):
        if board[idx_row][idx_column] == 1:
            return not can_t_attack

    return can_t_attack


def isSafe(row,
           column,
           oblique,
           oblique_inv,
           ctrl_line,
           ctrl_oblique,
           ctrl_obliqueinv):
    """Check if it is safe to put a queen at that position

    Args:
      row (int): row number
      column (int): column number
      oblique (array): for the diagionales
      oblique_inv (array): for the diagionales
      ctrl_line (array): for the rows
      ctrl_oblique (array): for the diagionales
      ctrl_obliqueinv (array): for the diagionales

    Returns:
      [boolean]: is-it safe to put a queen at that position
    """

    if ctrl_oblique[oblique[row][column]] or \
       ctrl_obliqueinv[oblique_inv[row][column]] or ctrl_line[row]:
        return False
    return True


def is_soluce(size, board):
    """Check if the board is one of the soluce.

    Args:
        size (int): size of the board
        board (array): content of the board

    Returns:
        [boolean]: is-it a solution ?
    """

    nbQueen = 0
    for row in range(size):
        for column in range(size):
            if board[row][column] == 1:
                nbQueen += 1

    for row in range(size):
        for column in range(size):
            if board[row][column] == 1 and \
               not queenCanTattack(board, size, row, column):
                return False

    if nbQueen == size:
        return True
    else:
        return False


def initCtrl(size):
    """Init array usefull to check the diagionales and the lines

    Args:
      size (int): size of the board

    Returns:
      [array]: ctrl_line
      [array]: ctrl_oblique
      [array]: ctrl_obliqueinv
    """

    x = 2 * size - 1
    ctrl_oblique = [False] * x
    ctrl_obliqueinv = [False] * x
    ctrl_line = [False] * size

    return ctrl_line, ctrl_oblique, ctrl_obliqueinv


def initObliques(size):
    """Init of array needed by ctrl_oblique and ctrl_obliqueinv

    Args:
      size (int): size of the board

    Returns:
      [array]: oblique
      [array]: oblique_inv
    """

    oblique = generateArray(size)
    oblique_inv = generateArray(size)

    for row in range(size):
        for column in range(size):
            oblique[row][column] = row + column
            oblique_inv[row][column] = row - column + (size - 1)

    return oblique, oblique_inv


def generateArray(size):
    """Return a 2D array full of 0.

    Args:
      size (int): number of row and number of column

    Returns:
      [array]: 2D array full of 0
    """

    return [[0 for x in range(size)] for y in range(size)]
