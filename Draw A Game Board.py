

NUM_HYPHENS = 3


def drawHyphens(n):
    for i in range(n):
        print(' ', end='', flush=True)
        for j in range(NUM_HYPHENS):
            print('-', end='', flush=True)
    print("\n", end='', flush=True)


def drawWalls(n):
    for i in range(n):
        print("|", end='', flush=True)
        for j in range(NUM_HYPHENS):
            print(' ', end='', flush=True)
    print("|")


def drawBoard(n):
    for i in range(n):
        drawHyphens(n)
        drawWalls(n)
    drawHyphens(n)


num = int(input("enter Num:"))

drawBoard(num)


