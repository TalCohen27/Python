string = input("enter string:")

result = 1

for i in range(0, int(string.__len__()/2)):
    if string[i] != string[string.__len__() - i - 1]:
            result = 0

if result == 1:
    print("this is a palindrome!")
else:
    print("this is NOT a palindrome!!")
