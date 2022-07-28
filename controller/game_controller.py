from view.game_view import GameView
from model.othello_game import OthelloGame

class GameController:
  def __init__(self, view: GameView, model: OthelloGame) -> None:
    self.view = view
    self.model = model

  def run_game(self):    
    #scores=[0,0]
    self.model.place_initial_pieces()
    while True: 
      self.view.draw_board()
      scores = self.model.calculate_score()
      self.view.display_score(scores)
      if self.model.is_terminated(scores=[0,0]):
        break
      curr_player = self.model.curr_player
      self.view.display_turn(curr_player)
      row, col = self.view.get_move()
      while self.model.make_move(row, col, curr_player) == False:
        row, col = self.view.get_move()
      self.model.change_player()

    player = self.model.find_winner()
    final_scores = self.model.calculate_score()
    self.view.display_winner(player, final_scores)
    self.model.write_results()
   


    


              