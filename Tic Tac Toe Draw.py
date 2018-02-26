
NUM_HYPHENS = 3
BOARD_SIZE = 3


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
    taken = True
    while taken:
        move = input("Player " + str(player) + " please make a move:")
        x = int(move.split(",")[0])
        y = int(move.split(",")[1])
        if game[x][y] == 0:
            game[x][y] = 'X' if player == 1 else 'O'
            taken = False
        else:
            print("place taken! Please choose another")


if __name__ == "__main__":
    game1 = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

    i1 = 0
    while True:
        updateBoard(game1)
        makeAMove(i1 % 2 + 1, game1)
        i1 += 1