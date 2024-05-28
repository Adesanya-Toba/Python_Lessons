# A Simple Python program to demonstrate working
# of yield.
"""
# The yield statement suspends a function's execution and
# sends a value back to the caller, but retains enough state
# to enable the function to resume where it left off. 
#
# When the function resumes, it continues execution immediately
# after the last yield run. This allows its code to produce a
# series of values over time, rather than computing them at once
# and sending them back like a list.
"""

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


from typing import Any, Generator, Literal, NoReturn


def simpleGeneratorFun() -> Generator[Literal[1, 2, 3], Any, None]:
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1


def nextSquare() -> Generator[int, Any, NoReturn]:
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)
