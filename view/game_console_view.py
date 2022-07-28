from model.players import Players
from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.othello_game import OthelloGame
from model.board import Board

class GameConsoleView(GameView):
  symbols = {0: ' ', 1: 'X', 2: 'O'}
  def __init__(self, game: OthelloGame) -> None:
    super().__init__(game)
    self.board_view = BoardConsoleView(game.board)
    self.game = game

  def display_score(self, scores):
    print(f'X score: {scores[0]} | O score: {scores[1]}\n')

  def display_turn(self, curr_player):
    print(f'Player {self.symbols[curr_player]}: It\'s your turn.')

  def get_move(self):
    s = input('Enter your move (row, col): ').split(',')
    row, col = int(s[0]), int(s[1])
    return row, col

  def draw_board(self):
    self.board_view.draw_board()

  def display_winner(self, player, scores):
    if player == 'X':
      print(f'Player X wins by {scores[0] - scores[1]} points.')
    elif player == 'O':
      print(f'Player O wins by {scores[1] - scores[0]} points.')
    else:
      print(f'The game ended in a tie. Both players have {scores[1]} points!')

