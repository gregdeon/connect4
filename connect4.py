# connect4.py
# Main class for Connect 4 interface

from basePlayer import *

class connect4(object):
    rows = 6
    cols = 7

    def __init__(self, player1, player2):
        # Board: a list of columns holding 0s (no move) or 1s or 2s
        self.board = [[0]*self.rows for i in range(self.cols)]
        # Height: how many pieces have been played in each column
        self.height = [0]*self.cols
        # Player modules: we ask these to pick their moves
        self.players = [player1, player2]

    def canMoveCol(self, col):
        # Check if we can play in column <col> (0-indexed)
        # Returns true if this is a legal move
        return self.height[col] < self.rows

    def move(self, player, col):
        # If possible, get player <player> to move in column <col>
        # Returns true if the move was successful
        if self.canMoveCol(col):
            self.board[col][self.height[col]] = player
            self.height[col] += 1
            return True
        return False

    def checkWin(self):
        # Check for wins all over the board
        for x in range(self.cols):
            for y in range(self.rows):
                checkWin = self.checkWinPosition(x, y)
                if checkWin != 0:
                    return checkWin

        return 0

    def checkWinPosition(self, x, y):
        # Check if there's a winner with a bottom-left-most piece 
        # at position (x, y)
        winner = self.board[x][y]

        # Can't win here if nobody's played it
        if winner == 0:
            return 0
        
        # Check for a win upwards
        if self.pieceAt(x, y+1) == winner and \
            self.pieceAt(x, y+2) == winner and \
            self.pieceAt(x, y+3) == winner:
            return winner

        # Check for a win rightwards
        if self.pieceAt(x+1, y) == winner and \
            self.pieceAt(x+2, y) == winner and \
            self.pieceAt(x+3, y) == winner:
            return winner

        # Check for a win up-right
        if self.pieceAt(x+1, y+1) == winner and \
            self.pieceAt(x+2, y+2) == winner and \
            self.pieceAt(x+3, y+3) == winner:
            return winner

        # Check for a win down-right
        if self.pieceAt(x+1, y-1) == winner and \
            self.pieceAt(x+2, y-2) == winner and \
            self.pieceAt(x+3, y-3) == winner:
            return winner

        # Nobody won!
        return 0

    def pieceAt(self, x, y):
        # Helper function for win-checking
        # Avoids going out of bounds, saving us some work
        if x < 0 or x >= self.cols:
            return 0
        if y < 0 or y >= self.rows:
            return 0
        return self.board[x][y]


    def printBoard(self):
        # Print the board to the screen
        for y in range(self.rows)[::-1]:
            s = ""
            for x in range(self.cols):
                s += str(self.board[x][y])
            print s

    def playGame(self):
        # The main game loop
        # Returns number of winning player (1 or 2)

        # Start: player 1 = index 0 
        player = 0
        while not self.checkWin():
            # TODO: check if we've reached a draw
            # Ask the player to move
            nextMove = self.players[player].move(self.board)

            # If invalid, ask them again 
            if nextMove < 0 or \
                nextMove >= self.cols or \
                not self.canMoveCol(nextMove):
                continue

            # Move is valid, so apply it
            self.move(player+1, nextMove)

            # Pick the next player
            if player == 0:
                player = 1
            else:
                player = 0

        # Check who the winner is
        return self.checkWin()

def main():
    player1 = basePlayer()
    player2 = basePlayer()
    c4 = connect4(player1, player2)
    winner = c4.playGame()

    # Game over
    c4.printBoard()
    print "Winner: Player {}!".format(winner)

if __name__ == "__main__":
    main()
