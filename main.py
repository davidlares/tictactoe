from board import Board

if __name__ == "__main__":

    board = Board()
    board.wipe_screen()

    while True:
        # Get X input
        x = int(input("\n X turn - Please choose [1 - 9]: "))
        board.set_choice(x,"X")

        if board.is_winner("X"):
            print("\n Congrats! X Player Wins! \n")
            break

        # Get O input (AI Intended)
        board.opponent_move("O") # default AI player
        board.wipe_screen() # showing "realtime results"
