##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 11/01/2020
# see: queen.py
##########################################

from soluce.queen import Queen


class Board:
    """A class to represent a board.

    Attributes:
        content (array) : content of the board
        size (int) : size of the board
        has_queen (boolean) : contains a queen
    Methods:
        getSize() - return the size of the board
        queensCanTattack() - check that none of the queens
        can attack each others
        getNumberOfQueen() - get the number of queen
    """

    def __init__(self, content, size):
        """Constructs all the necessary attributes for the board object.

        Args:
          content (array) : starting content of the board
          size (int) : size of the board
          has_queen (boolean) : contains a queen
          number_of_queen (int)
        """

        self.content = None
        self.size = size
        self.has_queen = False
        self.number_of_queen = 0
        self._setContent(content)

    def _setContent(self, content):
        """Setter for the content attribute,
        will put Queen objects at the place of the 1.

        Args:
          content (array): content of the board

        Returns:
          [array]: final starting content with the 1 remplace by Queen object
        """

        update = False
        for row in range(self.size):
            for column in range(self.size):
                if content[row][column] == 1:
                    content[row][column] = Queen(row, column)
                    self.number_of_queen += 1

                    if(not update):
                        self.has_queen = True
                        update = True

        self.content = content

    def getSize(self):
        """Get the size of the board.

        Returns:
          [int]: size of the board, knowing number of rows = number of columns
        """

        return self.size

    def getNumberOfQueen(self):
        """Get the number of queen on the board

        Returns:
          [int]: number of queen
        """

        return self.number_of_queen

    def queensCanTattack(self):
        """Check that none of the Queen objects on the board can attack each others.

        Returns:
          [boolean]: True if none of the queens can attack each others
        """

        can_t_attack = True
        if(not self.has_queen):
            return can_t_attack

        queens = self._getQueens()
        it = 0

        for attacker in queens:
            can_t_attack = self._checkDiagonals(attacker)

            if (can_t_attack):
                it += 1
                for victim in queens[it:len(queens)]:
                    if attacker.getPosX() == victim.getPosX() or \
                       attacker.getPosY() == victim.getPosY():
                        return not can_t_attack

        return can_t_attack

    def _getQueens(self):
        """Get all the queens on the board.

        Returns:
          [array]: contains all the Queen objects present on the board
        """

        queens = []
        nb_queen_found = 0
        for row in self.content:
            for column in row:
                if isinstance(column, Queen):
                    queens.append(column)
                    nb_queen_found += 1
                    if nb_queen_found == self.number_of_queen:
                        break

        return queens

    def _checkDiagonals(self, queen):
        """Check if the queen can't attack an other one on the diagonals

        Args:
          queen (Queen): instance of queen on the board

        Returns:
            [boolean]: False if can attack an other queen
        """

        for row, column in zip(range(queen.getPosY() - 1, -1, -1),
                               range(queen.getPosX() + 1, self.size)):
            if isinstance(self.content[row][column], Queen):
                return False

        for row, column in zip(range(queen.getPosY() + 1, self.size),
                               range(queen.getPosX() + 1, self.size)):
            if isinstance(self.content[row][column], Queen):
                return False

        for row, column in zip(range(queen.getPosY() - 1, -1, -1),
                               range(queen.getPosX() - 1, -1, -1)):
            if isinstance(self.content[row][column], Queen):
                return False

        for row, column in zip(range(queen.getPosY() + 1, self.size),
                               range(queen.getPosX() - 1, -1, -1)):
            if isinstance(self.content[row][column], Queen):
                return False

        return True

    def __repr__(self):
        """Representation of the board.

        Returns:
          [string]: return the content of the board as a string
        """

        return self._print()

    def _print(self):
        """Return the content of the board as a string.

        Returns:
          [string]: content of the board
        """

        display = ''

        for idx_row, row in enumerate(self.content):
            for idx_col, column in enumerate(row):
                display += ' '
                if (isinstance(column, Queen)):
                    display += column.getSymbol()
                else:
                    display += str(column)

                if idx_col == self.size - 1 and idx_row != self.size - 1:
                    display += '\n'

        return display
