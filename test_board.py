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

    # dummy filling X first row
    def filling_test_win(self):
        self.board.board.insert(1,"X")
        self.board.board.insert(2,"X")
        self.board.board.insert(3,"X")

    def test_board_length(self):
        self.assertEqual(len(self.board.board), 10)

    def test_validate_is_not_empty_cell(self):
        rand = random.randint(1,self.random_number)
        self.assertTrue(self.board.validate_cell(rand), True)

    def test_show_board(self):
        self.assertNotEqual(self.board.show_board(), False)

    def test_setting_choice(self):
        self.assertTrue(self.board.set_choice(self.random_number, self.default_player))

    # some winning case
    def test_winning_move(self):
        self.filling_test_win()
        for comb in [1,2,3]:
            if self.board.board[comb] == self.default_player:
                self.assertTrue(True, True)
            else:
                self.fail("At least one of the selection is empty or wrong")
                
if __name__ == "__main__":
    unittest.main() # execute all unittest
