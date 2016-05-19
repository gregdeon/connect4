# basePlayer.py
# A player class used by the Connect 4 module.
# Expand upon this to connect your own interface to the game.

class basePlayer(object):
    def __init__(self):
        pass

    def move(self, board):
        # The main move function.
        # Board is a 2D array containing the pieces in the board
        # 
        # move() must return a number in the range [0, 7) 
        # - Fill in your own method of choosing a move
        
        # Silly default: pick the first valid move we find
        for x in range(7):
            if board[x][5] == 0:
                return x
        # Should never get here...
        assert False
