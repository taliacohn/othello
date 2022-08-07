from copy import deepcopy
from model.rules import Rules
from model.symbols import Symbols
from model.player import Player

class Human(Player):
    """This class defines a human player"""
    def __init__(self, symbol: Symbols, board) -> None:
        super().__init__(symbol, board)
        self.rules = Rules(self.board)

    def give_hint(self, curr_player):
        lst_of_moves = self.rules.check_valid_moves(curr_player)
        for row, col in lst_of_moves:
            board_copy = deepcopy(self.rules.board.mat)
            board_copy[row][col] = '.'
        return board_copy
