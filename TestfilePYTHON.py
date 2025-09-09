# This is an example file to push to github

import math


def square(x):
    result = x * x
    return result


def squareroot(x):
    result = math.sqrt(x)
    return result

num = 8

squarednum = square(8)

print(f"The result of {num} squared is {squarednum} \n")
print(f"The square root of {squarednum} is {squareroot(squarednum):.0f}")

