BOARD_SIZE = 3


def checkRows(board):
    for i in range(0, BOARD_SIZE - 1):
        currCount = 1
        currChar = board[i][0]
        for j in range(0, BOARD_SIZE - 1):
            prevChar = currChar
            currChar = board[i][j+1]
            if currChar == prevChar:
                currCount += 1
            else:
                currCount = 0
            if currCount == BOARD_SIZE:
                return currChar
    return 0


def checkCols(board):
    for i in range(0, BOARD_SIZE - 1):
        currCount = 1
        currChar = board[0][i]
        for j in range(0, BOARD_SIZE - 1):
            prevChar = currChar
            currChar = board[j+1][i]
            if currChar == prevChar:
                currCount += 1
            else:
                currCount = 0
            if currCount == BOARD_SIZE:
                return currChar
    return 0


def checkMainDiag(board):
    currCount = 1
    currChar = board[0][0]
    for i in range(0, BOARD_SIZE - 1):
        prevChar = currChar
        currChar = board[i+1][i+1]
        if currChar == prevChar:
            currCount += 1
        else:
            currCount = 0
        if currCount == BOARD_SIZE:
            return currChar
    return 0


def checkSecondDiag(board):
    currCount = 1
    currChar = board[0][BOARD_SIZE - 1]
    for i in range(0, BOARD_SIZE - 1):
        prevChar = currChar
        currChar = board[i+1][BOARD_SIZE-(i+2)]
        if currChar == prevChar:
            currCount += 1
        else:
            currCount = 0
        if currCount == BOARD_SIZE:
            return currChar
    return 0


game = [[2, 1, 1],
	    [2, 1, 2],
	    [1, 2, 2]]

winner = 0

currResult = checkRows(game)
if currResult != 0:
    winner = currResult
currResult = checkCols(game)
if winner == 0 and currResult != 0:
    winner = currResult
currResult = checkMainDiag(game)
if winner == 0 and currResult != 0:
    winner = currResult
currResult = checkSecondDiag(game)
if winner == 0 and currResult != 0:
    winner = currResult

if winner != 0:
    print("The winner is player number", winner)
else:
    print("No winner!")


