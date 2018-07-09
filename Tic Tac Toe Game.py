
NUM_HYPHENS = 3
BOARD_SIZE = 3


def checkRows(board):
    for i in range(0, BOARD_SIZE-1):
        currCount = 1
        currChar = board[i][0]
        for j in range(0, BOARD_SIZE-1):
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
    for i in range(0, BOARD_SIZE-1):
        currCount = 1
        currChar = board[0][i]
        for j in range(0, BOARD_SIZE-1):
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
    for i in range(0, BOARD_SIZE-1):
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
    currChar = board[0][BOARD_SIZE-1]
    for i in range(0, BOARD_SIZE-1):
        prevChar = currChar
        currChar = board[i+1][BOARD_SIZE-(i+2)]
        if currChar == prevChar:
            currCount += 1
        else:
            currCount = 0
        if currCount == BOARD_SIZE:
            return currChar
    return 0


def drawHyphens(n):
    for i in range(n):
        print(' ', end='', flush=True)
        for j in range(NUM_HYPHENS):
            print('-', end='', flush=True)
    print("\n", end='', flush=True)


def drawWalls(n, game, rowIndex):
    for i in range(n):
        print("|", end='', flush=True)
        for j in range(NUM_HYPHENS):
            if j == 1 and game[rowIndex][i] != 0:
                print(game[rowIndex][i], end='', flush=True)
            else:
                print(' ', end='', flush=True)
    print("|")


def updateBoard(game):
    for i in range(BOARD_SIZE):
        drawHyphens(BOARD_SIZE)
        drawWalls(BOARD_SIZE, game, i)
    drawHyphens(BOARD_SIZE)


def makeAMove(player, game):
    invalid = True
    while invalid:
        move = input("Player " + str(player) + " please make a move: ")
        move_values = move.split(",")
        if len(move_values) != 2:
            print("Invalid format! "
                  "Please select an index in the format (comma separated): row,column")
        else:
            x = int(move_values[0])
            y = int(move_values[1])
            if x in range(0, BOARD_SIZE) and y in range(0, BOARD_SIZE):
                if game[x][y] == 0:
                    game[x][y] = 'X' if player == 1 else 'O'
                    invalid = False
                else:
                    print("place taken! Please choose another")
            else:
                print("Invalid index! Please select an index in the range: 0 to", BOARD_SIZE-1)


def checkForWinner(game):
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

    return winner


if __name__ == "__main__":

    gameBoard = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

    countLegalMoves = 0
    win = 0

    while win == 0 and countLegalMoves < BOARD_SIZE*BOARD_SIZE:
        updateBoard(gameBoard)
        makeAMove(countLegalMoves % 2 + 1, gameBoard)
        win = checkForWinner(gameBoard)
        countLegalMoves += 1

    updateBoard(gameBoard)

    if win != 0:
        print("The winner is player number", 1 if win == 'X' else 2)
    else:
        print("Game over, no winner!")