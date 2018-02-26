

print("Welcome to Hangman!")
hidden = ['-','-','-','-','-','-','-','-','-']
print("".join(hidden))
word = 'EVAPORATE'
find = False
indices = []

while not find:
    user_pick = input("Guess your letter:")
    indices = [i for i, letter in enumerate(word) if user_pick == letter]

    if len(indices) == 0:
        print("incorrect!")
    else:
        for index in indices:
            hidden[index] = user_pick
        print("".join(hidden))
        if hidden.count('-') == 0:
            find = True

print("good!")
