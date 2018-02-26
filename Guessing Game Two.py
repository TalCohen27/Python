import random


won = False
count = 0
left = 0
right = 99
mid = int((left + right)/2)

while not won:
    count += 1
    print(mid)
    userInput = input("Y, H  or L?")
    if userInput == "Y":
        won = True
    elif userInput == "H":
        left = mid + 1
    else:
        right = mid - 1
    mid = int((left + right)/2)

print("number of guesses:", count)
