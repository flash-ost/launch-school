"""
Isn't it Odd?
Write a function that takes one integer argument and returns True when the number's absolute value
is odd, False otherwise.
"""

def is_odd(number):
    # return True if abs(number) % 2 == 1 else False
    return True if number % 2 == 1 else False

print(is_odd(-533))