a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i, val in enumerate(a):
    if val < 5:
        print(val)

print([i for i in a if i < 5])

number = int(input("enter a number:"))

print([i for i in a if i < number])

for i in a:
    if i < 5:
        print(i)
