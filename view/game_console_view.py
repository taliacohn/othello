from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.othello_game import OthelloGame

class GameConsoleView(GameView):
  symbols = {0: ' ', 1: 'X', 2: 'O'}
  def __init__(self, game: OthelloGame) -> None:
    super().__init__(game)
    self.board_view = BoardConsoleView(game.board)
    self.game = game

  # def board_size_error():
  #   print('Please enter a positive number that is above 3 and is a multiple of 2'
  #     '(ex/ 4, 8, 12).')

  def welcome_message():
    print('-------------------------------------------')
    print('------------Welcome to Reversi!------------')
    print('-------------------------------------------')
    try:
      board_size = int(input('Enter board size: '))
    except ValueError:
      print('Please enter a positive number that is above 3 and is a multiple of 2'
      '(ex/ 4, 8, 12).')
      board_size = int(input('Enter board size: '))
    if board_size > 2 and board_size % 2 == 0:
      return board_size
    else:
      print('Please enter a positive number that is above 3 and is a multiple of 2'
      '(ex/ 4, 8, 12).')
      return int(input('Enter board size: '))

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
        s = s.replace(',', '')
        s = s.replace(' ', '')
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
    if player == 1:
      print(f'Player X wins by {scores[0] - scores[1]} points.')
    elif player == 2:
      print(f'Player O wins by {scores[1] - scores[0]} points.')
    else:
      print(f'The game ended in a tie. Both players have {scores[1]} points!')

  def display_exit_message(self):
    print('Thanks for playing.\n')

  def display_play_again(self):
    s = input('Do you want to play again? ').lower()
    if s == 'no'.startswith('n'):
      return 1

  def display_empty_line(self):
    print('')
    
  def display_rules(self):
    print('')
    print('-' * 70)
    print('------------------------------Game Rules------------------------------')
    print('-' * 70)
    print('Choose an empty square to place your symbol (X or O).')
    print('')
    self.game.new_board()
    self.game.board.initial_position()
    self.board_view.draw_board(self.game.board.mat)
    print('')
    print('Make sure at least one of your opponent\'s pieces are trapped between yours!')
    print('')
    ex_board1 = self.game.board.example_board()
    self.board_view.draw_board(ex_board1)
    print('')
    print('The captured piece switches to the other symbol...')
    print('')
    ex_board2 = self.game.board.example_board_with_move()
    self.board_view.draw_board(ex_board2)
    print('')
    print('If you can\'t trap a piece, you lose your turn!')
    print('You can request a hint at any time by typing \'hint\'.')
    print('Entering hint will show a board with the current pieces and . to represent available moves.')
    print('')
    ex_board3 = self.game.board.example_board_hint()
    self.board_view.draw_board(ex_board3)
    print('')
    print('Exit the game on your turn by typing \'exit\'!')
    print('')
    print('If a player has no available moves, their turn will be skipped until there is a possible move.')
    print('Pieces are counted at the end of the game. Player with the most pieces wins!')
    print('Good luck!')
    print('')

  def get_depth(self):
    try:
      depth = int(input("Enter level of difficulty (any number): "))
      return depth
    except:
      if depth != int:
        print('Invalid response. Numbers only.')
        depth = int(input("Enter level of difficulty (any number): "))
   
