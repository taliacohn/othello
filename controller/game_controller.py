from model.ai import AI
from model.human import Human
from model.symbols import Symbols
from view.game_view import GameView
from model.othello_game import OthelloGame


class GameController:
  def __init__(self, view: GameView, model: OthelloGame) -> None:
    self.view = view
    self.model = model
    self.simple_ai = AI()

  def run_game(self):    
    self.view.welcome_message()
    while True: #new game until exit is selected
      players = []
      player_choice = self.view.player_options()
      #scores=[0,0]
      if player_choice == 1:
        players.append(Human(Symbols.X))
        #display player 1: you are X
        players.append(Human(Symbols.O))
        #display player 2: you are O
      elif player_choice == 2:
        players.append(Human(Symbols.X))
        players.append(AI(Symbols.O))
      elif player_choice == 3:
        pass 
          #Minimax
      elif player_choice == 4:
        #display rules
        pass
      elif player_choice == 5: #exit game 
        self.view.display_exit_message()
        return False
      
      #initialize board
      self.model.curr_player = self.model.rules.first_move() #which symbol goes first
      self.model.new_board()
      self.model.place_initial_pieces()
      
      while True: 
        board = self.view.draw_board()
        scores = self.model.rules.calculate_score()
        self.view.display_score(scores)
        curr_player = self.model.curr_player #gives 1 or 2 for symbol
        if self.model.rules.is_terminated(curr_player, scores=[0,0]) == False:
          break
        
        self.view.display_turn(curr_player)

        if isinstance(player[curr_player-1], AI):
          self.view.display_computer_turn()
          row, col = self.simple_ai.ai_simple_move()
          self.model.rules.make_move(row, col, curr_player, board)
        else:
          row, col = self.view.get_move()

          while self.model.rules.make_move(row, col, curr_player, board) == False:
            self.view.invalid_move()
            row, col = self.view.get_move()
        
        self.model.rules.change_player()

      player = self.model.find_winner()
      final_scores = self.model.rules.calculate_score()
      self.view.display_winner(player, final_scores)
      self.model.write_results()
   


    


              