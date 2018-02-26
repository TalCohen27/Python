import random


with open('sowpods.txt', 'r') as f:
    allLines = f.readlines()
    numLines = len(allLines)
    randomNum = random.randint(0, numLines)
    print(allLines[randomNum].strip())

