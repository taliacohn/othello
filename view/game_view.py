from abc import ABC, abstractmethod
from model.othello_game import OthelloGame

class GameView(ABC):
    
    def __init__(self, game) -> None:
        self.game = game

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_turn(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass

    @abstractmethod
    def display_score(self, score):
        pass