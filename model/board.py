from pickle import EMPTY_DICT
from model.symbols import Symbols

class Board:
  """Board and board size"""
  EMPTY_CELL = 0

  def __init__(self, size=8) -> None:
    self.size = size
    self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]

  def get_cell(self, row, col):
    return self.mat[row-1][col-1]

  def update_cell(self, row, col, player):
    self.mat[row-1][col-1] = player
   

  def initial_position(self):
    """Starting position of initial 4 pieces on board"""
    split_board = self.size//2
    #Piece 1, player 1
    self.update_cell(split_board, split_board, Symbols.X)
    #Piece 1, player 2
    self.update_cell(split_board, split_board+1, Symbols.O)
    #Piece 2, player 1
    self.update_cell(split_board+1, split_board+1, Symbols.X)
    #Piece 2, player 2
    self.update_cell(split_board+1, split_board, Symbols.O)

  def new_board(self):
    for i in range(2, self.size):
      for j in range(2, self.size):
        self.update_cell(i, j, 0)
    
    self.mat
    








