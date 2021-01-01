##########################################
# author: MEZROUI Marwan, BULTEZ Victor
# created: 01/01/2021
# modified: 01/01/2021
##########################################
from soluce.queen import Queen

def test_getPos():
  queen = Queen(5,8)
  assert queen.getPosX() == 5
  assert queen.getPosY() == 8


def test_getSymbol():
  queen = Queen(0,0)
  assert queen.getSymbol() == 1