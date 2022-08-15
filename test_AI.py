import unittest
from model.othello_game import OthelloGame
from model.symbols import Symbols
from model.board import Board

class TestAI(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.game = OthelloGame(4)

    def test_simple_ai_move(self):
        #actual_moves = self.game.rules.check_valid_moves(Symbols.O)
        game = OthelloGame(4)
        game.place_initial_pieces()
        game.rules.curr_player = Symbols.O
        curr_player = game.rules.curr_player
        actual_moves = game.rules.check_valid_moves(curr_player)
        expected_moves = [(0, 2), (2, 0), (1, 3), (3,2)]
        self.assertTrue(game.simple_ai.ai_simple_move(curr_player) in actual_moves)