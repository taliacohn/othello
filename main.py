from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.othello_game import OthelloGame
from model.rules import Rules

model = OthelloGame(board_size=8)
view = GameConsoleView(model)

controller = GameController(view, model)

controller.run_game()
