#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l_digit = abs(number) % 10
if (number < 0):
    l_digit *= -1

if (l_digit == 0):
    line = "and is 0"
elif (l_digit > 5):
    line = "and is greater than 5"
elif (l_digit < 6 and l_digit != 0):
    line = "and is less than 6 and not 0"
print("Last digit of", number, "is", l_digit, line)
