import unittest
import random
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        # dummy test values
        self.random_number = random.randint(1, len(self.board.board))
        self.default_player = "X"

    def tearDown(self):
        pass

    def test_board_length(self):
        self.assertEqual(len(self.board.board), 10)

    def test_show_board(self):
        self.assertNotEqual(self.board.show_board(), False)

    def test_setting_choice(self):
        self.assertTrue(self.board.set_choice(self.random_number, self.default_player))

if __name__ == "__main__":
    unittest.main() # execute all unittest
