import random

randomNumber = random.randint(1, 10)
exited = ""
count = 0

while exited != "exit":
    num = int(input("enter number:"))
    count += 1
    if num == randomNumber:
        print("correct")
    elif num < randomNumber:
        print("Too low!")
    else:
        print("Too high!")

    exited = input("type exit if you want to")

print("number of guesses:", count)
