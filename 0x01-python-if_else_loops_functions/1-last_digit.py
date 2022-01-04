#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end="")
if number < 0:
    number = (number * -1 % 10) * -1
else:
    number = number % 10
if number > 5:
    print("{} and is greater than 5".format(number))
elif number == 0:
    print("{} and is 0".format(number))
elif number < 6:
    print("{} and is less than 6 and not zero".format(number))
