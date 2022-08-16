import unittest
from model.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(8)
        self.game_board = self.board.mat

    def test_update_cell(self):
        self.board.update_cell(3, 6, 'X')
        self.assertEqual(self.board.get_cell(3, 6), 'X')

    def test_get_cell(self):
        self.board.update_cell(4, 5, 'O')
        self.assertEqual(self.board.get_cell(4, 5), 'O')
        self.assertNotEqual(self.board.get_cell(3, 6), 'X')


