number = int(input("enter a number:"))

print([i for i in range(1, number+1) if number % i == 0])
