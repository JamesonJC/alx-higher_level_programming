#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
l_d = (-number) % 10
if l_d > 5:
    print(f"Last digit of {number} is {l_d} and is greater than 5")
if l_d == 0:
    print("Last digit of {number} is {l_d} and is 0")
if l_d < 6 and l_d != 0:
    print("Last digit of {number} is {l_d} and is less than 6 and not 0")
