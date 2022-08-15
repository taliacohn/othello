import unittest
from model.board import Board

class TestBoard(unittest.TestCase):
    @classmethod
    def setUpModule(cls):
       cls.board = Board()

    def test_update_cell(self):
        self.board.update_cell(3, 6, 'X')
        self.assertEqual(self.board.get_cell(3, 6), 'X')

    def test_get_cell(self):
        self.assertEqual(self.board.get_cell(4, 5), 0)
        self.assertEqual(self.board.get_cell(3, 6), 'X')


