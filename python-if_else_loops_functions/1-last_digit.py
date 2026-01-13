#!/usr/bin/python3
import random
numb = random.randint(-10000, 10000)
last_digit = numb % 10 if numb >= 0 else (numb % 10 - 10)
if last_digit > 5:
    print(f"Last digit of {numb} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {numb} is {last_digit} and is 0")
else:
    print(f"Last digit of {numb} is {last_digit} and is less than 6 and not 0")
