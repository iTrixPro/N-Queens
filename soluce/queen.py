##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 11/01/2020
##########################################


class Queen:
    """A class to represent a queen.

    Attributes:
        positionX (int) : its horizontal position on the board
        positionY (int) : its vertical position on the board
        symbol (int) : its symbol on the board
    Methods:
        getPosX() - return its horizontal position
        getPosY() - return its vertical position
        getSymbol() - return its symbol
    """

    def __init__(self, y, x):
        """Constructs all the necessary attributes for the queen object.

        Args:
          positionX (int): horizontal position
          positionY (int): vertical position
          symbol (int): representation on the board
        """

        self.positionX = x
        self.positionY = y
        self.symbol = 1

    def getPosX(self):
        """Get its horizontal position on the board.

        Returns:
          [int]: horizontal position
        """

        return self.positionX

    def getPosY(self):
        """Get its vertical position on the board.

        Returns:
          [int]: vertical position
        """

        return self.positionY

    def getSymbol(self):
        """Get its representation in the board.

        Returns:
          [int]: on the board the queen is represent by an int
        """

        return self.symbol
