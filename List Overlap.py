import random

a = [random.randrange(1, 100, 1) for i in range(0, 12, 1)]
b = [random.randrange(1, 50, 1) for i in range(0, 14, 1)]

print(a)
print(b)

test = list(set(a).intersection(set(b)))

if test:
    print("The intersections are: ", test)
else:
    print("No intersection.")
