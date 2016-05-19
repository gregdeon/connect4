# humanPlayer.py
# A player module that asks for moves on the command line

from basePlayer import *
import util

class humanPlayer(basePlayer):
    def __init__(self):
        pass

    def move(self, board):
        # Show the user the board 
        util.printBoard(board)
        print ""
    
        # Ask for their next move until we get a valid one
        while True:
            try:
                # Ask for move
                nextMove = int(raw_input("Your move: "))

                # Check values
                if nextMove < 1 or \
                    nextMove > 7 or \
                    board[nextMove-1][5] != 0:
                    raise ValueError()

                return nextMove-1
            except:
                print "Invalid move - try again!"
