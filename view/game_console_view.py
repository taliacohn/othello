from typing_extensions import Self
from model.symbols import Symbols
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

  # def welcome_message(self):
  #   print('-------------------------------------------')
  #   print('------------Welcome to Reversi!------------')
  #   print('-------------------------------------------')

  def welcome_message():
    print('-------------------------------------------')
    print('------------Welcome to Reversi!------------')
    print('-------------------------------------------')
    try:
      board_size = int(input('Enter board size: '))
    except ValueError:
      board_size = int(input('Please enter a positive number that is above 3 and is a multiple of 2'
      '(ex/ 4, 8, 12).\nEnter board size: '))
    if board_size > 2 and board_size % 2 == 0:
      return board_size
    else:
      return int(input('Please enter a positive number above 2 (ex/ 8).\nEnter board size: '))

  def no_moves(self):
    print('No valid moves. Switching players.')

  def player_options(self):
    """Player inputs how many players - 1 vs 2 human players"""
    choice = -1
    while 0 > choice < 3:
      try:
        choice = int(input('Select Game Mode: \n1. Player vs Player\n2. Player vs Simple Computer'
        '\n3. Player vs Difficult Computer\n4. Rules\n5. Exit game\nEnter your choice (1, 2, 3, 4, or 5): '))
      except:
        print('Invalid option. Please enter 1, 2, 3, 4 or 5.')
    return choice
    
  def invalid_choice(self):
    print('Invalid option.')

  def display_score(self, scores):
    print(f'X score: {scores[0]} | O score: {scores[1]}\n')

  def display_turn(self, curr_player):
    print(f'Player {self.symbols[curr_player]}: It\'s your turn.')

  def display_rules(self):
    pass

  def get_move(self, curr_player): #add option to ask for hint
    """Asks player for next move. Allow player to exit game or ask for hint. Provide feedback 
    if incorrect move inputted."""
    
    s = input('Enter your move (row, col), \'exit\' to end game, or \'hint\' for a hint: ')
    s = s.lower()
    if s == 'exit':
      return 'exit'
    elif s == 'hint':
      return 'hint'
    else:
      try:
        s = s.split(', ')
        row, col = int(s[0]), int(s[1])
        return row, col
      except:
        print('Enter two numbers separated by a comma. For example, \'3, 2\'.')
        return self.get_move(curr_player)
      
  def display_computer_turn(self):
    print('---------------------------')
    print('The computer is thinking...')
    input('Press enter to see the computer\'s move. ')

  def invalid_move(self):
    """If player makes makes an invalid move"""
    print('Not a valid move. Remember there needs to be a line between one of your pieces',
            'and the piece you put down, with your opponent\'s piece(s) in between.')
    
  def draw_board(self, mat):
    self.board_view.draw_board(mat)

  def display_winner(self, player, scores):
    if player == 'X':
      print(f'Player X wins by {scores[0] - scores[1]} points.')
    elif player == 'O':
      print(f'Player O wins by {scores[1] - scores[0]} points.')
    else:
      print(f'The game ended in a tie. Both players have {scores[1]} points!')

  def display_exit_message(self):
    print('Thanks for playing.\n')

  def display_play_again(self):
    pass 

  def display_empty_line(self):
    print('\n')
    