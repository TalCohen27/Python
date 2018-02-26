winner = "None"

while winner == "None":
        A = input("enter player A:")
        B = input("enter player B:")
        if (A == "R" and B == "S") or (A == "P" and B == "R") or (A == "S" and B == "P"):
            winner = "A"
        elif A != B:
            winner = "B"

print("The winner is", winner)






