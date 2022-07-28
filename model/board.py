from pickle import EMPTY_DICT
from model.players import Players

class Board:
  """Board and board size"""
  EMPTY_CELL = 0

  def __init__(self, size) -> None:
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
    self.update_cell(split_board, split_board, Players.X)
    #Piece 1, player 2
    self.update_cell(split_board, split_board+1, Players.O)
    #Piece 2, player 1
    self.update_cell(split_board+1, split_board+1, Players.X)
    #Piece 2, player 2
    self.update_cell(split_board+1, split_board, Players.O)




