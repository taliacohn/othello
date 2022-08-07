from model.rules import Rules
from model.player import Player
from model.symbols import Symbols
#from model.othello_game import OthelloGame
from copy import deepcopy


class AI(Player):
    def __init__(self, symbol: Symbols, board) -> None:
        super().__init__(symbol, board)
        self.rules = Rules(self.board)
        
    def ai_simple_move(self, curr_player):
        lst_of_moves = self.rules.check_valid_moves(curr_player) #get a list of possible moves 
        highest_score = -1
        for row, col in lst_of_moves:
            board_copy = deepcopy(self.rules.board.mat)
            self.rules.make_move(row, col, curr_player)
            score = self.rules.calculate_score()
            curr_score = score[1]
            if curr_score > highest_score:
                move = [row, col]
                highest_score = curr_score
            self.rules.board.mat = board_copy
        return move






