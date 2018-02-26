import random


def findOccur(s, ch, usedIndex):
    return [i for i, letter in enumerate(s) if letter == ch and i not in usedIndex]


def countCowsAndBulls(a, b):
    countCows = 0
    countBulls = 0
    usedIndexA = set()
    usedIndexB = set()
    length = len(a)
    for i in range(0, length):
        indexOfCharA = frozenset(findOccur(a, strRand[i], usedIndexA))
        indexOfCharB = frozenset(findOccur(b, strRand[i], usedIndexB))
        usedIndexA.update(indexOfCharA)
        usedIndexB.update(indexOfCharB)
        countCows += len(indexOfCharA.intersection(indexOfCharB))
        lenB = len(indexOfCharB.difference(indexOfCharA))
        lenA = len(indexOfCharA.difference(indexOfCharB))
        countBulls += min(lenB, lenA)
    print(countCows, "cows", countBulls, "bulls")
    return True if countCows == length else False


if __name__ == "__main__":
    rand = random.randint(1000, 9999)
    countGuesses = 0
    strRand = str(rand)
    isWin = False

    while not isWin:
        user_num = input("Give me a 4 digit number: ")
        isWin = countCowsAndBulls(strRand, user_num)
        countGuesses += 1

    print("You won after", countGuesses, "guesses! The number was indeed", rand)