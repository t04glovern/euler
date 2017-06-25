"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def evenly_divisible(value):
    for x in range(1, 21):
        if value % x != 0:
            return False
    return True

a = 1
while 1:
    if evenly_divisible(a):
        print(a)
        break
    else:
        a = a + 1
