from model.ai import AI
from model.ai_minimax import AdvancedAI
from view.game_view import GameView

from model.othello_game import OthelloGame

class GameController:
  def __init__(self, view: GameView, model: OthelloGame) -> None:
    self.view = view
    self.model = model
    
  def run_game(self):    
    while True: #new game until exit is selected
      players = []
      self.view.display_empty_line()
      player_choice = self.view.player_options()

      players.append(self.model.human)
      if player_choice == 1:
        players.append(self.model.human)
      elif player_choice == 2:
        players.append(self.model.simple_ai)
      elif player_choice == 3:
        depth = self.view.get_depth()
        players.append(self.model.advanced_ai)
      elif player_choice == 4:
        self.view.display_rules()
        player_choice = self.view.player_options()
      elif player_choice == 5: 
        self.view.display_exit_message()
        return False
      
      #initialize board
      self.model.rules.curr_player = self.model.rules.first_move() #which symbol goes first
      self.model.new_board()
      self.model.place_initial_pieces()
      
      game_mode = True
      while game_mode: 
        self.view.display_empty_line()
        self.view.draw_board(self.model.board.mat)
        scores = self.model.rules.calculate_score()
        self.view.display_score(scores)
        curr_player = self.model.rules.curr_player #gives 1 or 2 for symbol
        if self.model.rules.is_terminated(curr_player, scores) == False:
          break
        
        self.view.display_turn(curr_player)

        if isinstance(players[curr_player-1], AI) or isinstance(players[curr_player-1], AdvancedAI):
          self.view.display_computer_turn()
          if player_choice == 2:
            move = self.model.simple_ai.ai_simple_move(curr_player)
          elif player_choice == 3:
            move = self.model.advanced_ai.choose_move(depth)

          if move == 1:
            self.view.no_moves()
            continue
          else:
            self.model.rules.make_move(move[0], move[1], curr_player)
          
        else:
          #try:
          move = True
          while move:
            move = self.view.get_move(curr_player)
            if move == 'exit':
              self.view.display_empty_line()
              self.view.display_exit_message()
              move = False
              game_mode = False
              #return self.model.rules.is_terminated(curr_player) == True
            elif move == 'hint': 
              hint_board = self.model.human.give_hint(curr_player)
              if hint_board == 1:
                self.view.no_moves()
                continue
              else:
                self.view.draw_board(hint_board)
                self.view.display_empty_line()
            else:
              while self.model.rules.make_move(move[0], move[1], curr_player) == False:
                self.view.invalid_move()
                move = self.view.get_move(curr_player)
              break
        
        self.model.rules.change_player()

      if self.model.rules.is_terminated(curr_player, scores) == False:
        player = self.model.rules.find_winner()
        final_scores = self.model.rules.calculate_score()
        self.view.display_winner(player, final_scores)
        self.view.display_empty_line()
        self.model.write_results()

      if self.view.display_play_again() == 1:
        self.view.display_exit_message()
        break

