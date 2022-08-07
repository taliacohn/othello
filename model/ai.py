from model.rules import Rules
from model.board import Board
from model.player import Player

from copy import deepcopy

class AI(Player):
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.board = Board()
        self.game = Rules(self.board)
        
    def ai_simple_move(self, curr_player):
        lst_of_moves = self.game.check_valid_moves(curr_player) #get a list of possible moves 
        highest_score = -1
        for row, col in lst_of_moves:
            board_copy = deepcopy(self.board.mat)
            self.game.make_move(row, col, curr_player, board_copy)
            score = self.game.calculate_score()
            if score > highest_score:
                move = [row, col]
                highest_score = score
        return move






