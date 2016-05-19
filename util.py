# util.py
# Utility for printing the game state onto the screen

def printBoard(board):
    # Print a board onto the screen
    # TODO: think about coloring the 1s and 2s
    for y in range(len(board[0]))[::-1]:
        s = ""
        for x in range(len(board)):
            if board[x][y] == 0:
                s += "."
            else:
                s += str(board[x][y])
        print s
