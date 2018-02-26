from datetime import datetime

try:
    name = input('Please enter your name:')
    age = int(input('Your age:'))
    number = int(input('Enter any number:'))
except ValueError:
    print("Not a number")

now = datetime.now()

for x in range(0, number):
    print("In the year %s you'll turn 100 years old" % (100-age + now.year - 1))



