import os
import time
import random

class Board():
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def wipe_screen(self):
        #os.system("clear") # UNIX Os Only
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Welcome to TicTacToe Game \n")
        self.show_board()

    # empty validation
    def validate_cell(self, cell):
        return True if self.board[cell].startswith(" ") else False

    def show_board(self):
        print(" %s | %s | %s  " %(self.board[1],self.board[2], self.board[3]))
        print("-----------")
        print(" %s | %s | %s  " %(self.board[4],self.board[5], self.board[6]))
        print("-----------")
        print(" %s | %s | %s  " %(self.board[7],self.board[8], self.board[9]))
        return True

    def set_choice(self, choice, player):
        if self.validate_cell(choice):
            self.board[choice] = player
        else:
            print(" Cell Already took. Missing turn. Please wait \n")
            time.sleep(3) # delaying response for watching messages
            return False
        return True

    def opponent_move(self, player):
        rand = random.randint(1,9)
        if self.validate_cell(rand):
            self.set_choice(rand, player)
        else:
            print(" AI picked a cell already took. Missing turn. Please wait \n")
            time.sleep(3) # delaying response for watching messages
            return False
