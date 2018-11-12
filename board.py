import os

class Board():
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def wipe_screen(self):
        os.system("clear") # UNIX Os Only
        print("\n Welcome to TicTacToe Game \n")
        self.show_board()

    def show_board(self):
        print(" %s | %s | %s  " %(self.board[1],self.board[2], self.board[3]))
        print("-----------")
        print(" %s | %s | %s  " %(self.board[4],self.board[5], self.board[6]))
        print("-----------")
        print(" %s | %s | %s  " %(self.board[7],self.board[8], self.board[9]))
        return True
