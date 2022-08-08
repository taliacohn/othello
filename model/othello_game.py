from model.ai import AI
from model.board import Board
from model.symbols import Symbols

from datetime import datetime
from model.results_text_file import ResultsTextFile
from model.rules import Rules

from model.human import Human

class OthelloGame():
    """This class represents the Othello game, includes methods
    to run the game"""
    #DIRECTIONS = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def __init__(self, board_size=8, file_path="results_of_game.txt") -> None:
        self.board = Board(board_size)
        self.board_size = board_size
        self.save_game = ResultsTextFile(file_path)
        self.rules = Rules(self.board, board_size)
        self.simple_ai = AI(Symbols.O, self.board, self.board_size)
        self.human = Human(Symbols, self.board, self.board_size)
        
    def new_board(self):
        """Displays a new board with four initial pieces"""
        return self.board.new_board()

    def place_initial_pieces(self):
        """Places four starting pieces on the board"""
        return self.board.initial_position()

    def find_winner(self):
        score = self.rules.calculate_score()
        if score[0] > score[1]:
            self.winner = 'X'
        elif self.score[1] > self.score[0]:
            self.winner = 'O'
        else:
            self.winner = 'It\'s a tie!'

        return self.winner

    def write_results(self):
        self.score = self.rules.calculate_score()
        today = datetime.now()
        time = today.strftime('%m/%d/%Y %H:%M:%S')
        self.results = f'Date and time of game: {time} | '
        self.results += f'Winner of game: {self.winner} | '
        self.results += f'Player X: {self.score[0]}, Player O: {self.score[1]}\n'
        
        return self.save_game.save_results(self.results)
        

        
        




            





   
        


