##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# created: 18/12/2020
# modified: 05/01/2020
##########################################

def backtracking(board, size):
    """Algo to solve the problem. Deprecated for a size superior at 20.

    Args:
        board (Board)
        size (int): size of the board

    Returns:
        [Board]: board with the solution
        [boolean]: success to find a solution
    """
    nb_queen = board.getNumberOfQueen()
    if nb_queen == size:
        return board, True

    for row in range(size):
        if board.queenCanTattack(row, nb_queen):
            board.add(row, nb_queen)
            board, solved = backtracking(board, size)
            if solved:
                return board, solved
            board.remove(row, nb_queen)

    return board, False