from board import Board
import unittest

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def tearDown(self):
        pass

    def test_board_length(self):
        self.assertEqual(len(self.board.board), 10)

    def test_show_board(self):
        self.assertNotEqual(self.board.show_board(), False)

if __name__ == "__main__":
    unittest.main() # execute all unittest
