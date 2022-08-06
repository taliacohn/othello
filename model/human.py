# from model.othello_game import OthelloGame
# from model.board import Board
# from model.symbols import Symbols
from model.player import Player
#from model.rules import Rules

class Human(Player):
    """This class defines a human player"""
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        

    def give_hint(self):
        pass
        