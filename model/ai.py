from model.board import Board
from model.rules import Rules
from model.player import Player
#from model.othello_game import OthelloGame

from copy import deepcopy
from numpy import Infinity

class AI(Player):
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.rules = Rules
        
    def ai_simple_move(self, curr_player):
        lst_of_moves = self.rules.check_valid_moves(curr_player) #get a list of possible moves 
        highest_score = -Infinity
        for row, col in lst_of_moves:
            board_copy = deepcopy(self.rules.board.mat)
            self.rules.make_move(row, col, curr_player, board_copy)
            score = self.rules.calculate_score()
            if score > highest_score:
                move = [row, col]
                highest_score = score
        return move






