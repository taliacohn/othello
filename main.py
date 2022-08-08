from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.othello_game import OthelloGame

board_size = GameConsoleView.welcome_message()
model = OthelloGame(board_size)
view = GameConsoleView(model)

controller = GameController(view, model)

controller.run_game()
