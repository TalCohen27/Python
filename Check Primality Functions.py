import math


def get_num_divisors(num):
    return sum([i for i in range(2, number) if number % i == 0])


number = int(input("enter a number:"))

if get_num_divisors(number):
    print("not prime")
else:
    print("is a prime")

print(sum([True if number % factor == 0 else False for factor in ([2] + list(range(3, int(math.sqrt(number)), 2)))]))