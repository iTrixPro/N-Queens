##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# modified: 11/01/2021
##########################################
from soluce.queen import Queen


def test_getPos():
    queen = Queen(5, 8)
    assert queen.getPosX() == 8
    assert queen.getPosY() == 5


def test_getSymbol():
    queen = Queen(0, 0)
    assert queen.getSymbol() == 1
