import random


def pickRandomWord():
    with open('sowpods.txt', 'r') as f:
        allLines = f.readlines()
        numLines = len(allLines)
        randomNum = random.randint(0, numLines)
        return allLines[randomNum].strip()


def findLetters(searchLetter, wordToScan, hiddenWord):
    result = False
    indices = [i for i, letter in enumerate(wordToScan) if searchLetter == letter]
    if len(indices) == 0:
        print("incorrect!")
    else:
        for index in indices:
            hiddenWord[index] = searchLetter
        result = True
        print("".join(hiddenWord))
    return result


def getLetterFromUser(usedLetters):
    used = True
    while used:
        user_choice = input("Guess your letter:")
        if user_choice in usedLetters:
            print("You already guessed that letter! Pick a new one")
            used = True
        else:
            usedLetters.add(user_choice)
            used = False
    return user_choice


if __name__ == "__main__":
    randomWord = pickRandomWord()
    print("Welcome to Hangman!")
    hidden = ['-' for i in range(len(randomWord))]
    print("".join(hidden))
    count = 6

    correct = False
    win = False
    usedChars = set()

    while not win:
        print("you got ", count, "incorrect guesses left!")
        user_pick = getLetterFromUser(usedChars)
        correct = findLetters(user_pick, randomWord, hidden)
        if not correct:
            count -= 1
        if count == 0:
            print("you lose!")
            break
        if hidden.count('-') == 0:
            win = True
if win:
    print("you won!")






